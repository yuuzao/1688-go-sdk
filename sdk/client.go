package sdk

import (
    "context"
    "crypto/sha1"
    "encoding/hex"
    "fmt"
    "net/http"
    "net/url"
    "slices"
    "strings"
    "time"
)

// Client SDK 客户端，线程安全，可复用
type Client struct {
    server string // 例如 gw.open.1688.com 或 127.0.0.1:port

    appKey string
    secret string

    http   Doer
    logger Logger

    tsSource      TimestampSource
    tokenProvider AccessTokenProvider

    userAgent string
    timeout   atomicDuration
    redact    RedactConfig
}

// NewClient 使用函数式选项构建客户端
func NewClient(opts ...Option) *Client {
    c := &Client{
        http:      &http.Client{},
        logger:    NopLogger{},
        tsSource:  LocalClock(),
        userAgent: "Ocean-SDK-Client",
        redact:    defaultRedact(),
    }
    for _, opt := range opts { opt(c) }
    return c
}

// Do 模板方法：参数收集 -> 校验 -> 系统参数注入 -> 签名 -> 选择编码 -> 发送请求 -> 解析与错误判定。
func (c *Client) Do(ctx context.Context, req APIRequest, out any) error {
    if c.server == "" { return &AopError{Kind: "param", Message: "server not set"} }
    api := req.API().URI
    if api == "" { return &AopError{Kind: "param", Message: "api uri empty"} }

    // 准备参数：复制业务参数
    params := map[string]any{}
    for k, v := range req.Params() { params[k] = v }

    // 必填校验（仅业务参数）
    missing := missingKeys(params, req.RequiredParams())
    if len(missing) > 0 {
        return &AopError{Kind: "param", Message: fmt.Sprintf("required params missing: %v", missing), APIURI: api}
    }

    // 系统参数注入
    // timestamp
    var ts string
    if req.NeedTimestamp() {
        t, err := c.tsSource.NowMillis(ctx, c)
        if err != nil { return &AopError{Kind: "time", Message: err.Error(), APIURI: api} }
        ts = fmt.Sprintf("%d", t)
        params["_aop_timestamp"] = ts
    }

    // access_token
    var token string
    if req.NeedAuth() {
        if c.tokenProvider == nil { return &AopError{Kind: "auth", Message: "token provider not set", APIURI: api} }
        tok, err := c.tokenProvider.Token(ctx)
        if err != nil { return &AopError{Kind: "auth", Message: err.Error(), APIURI: api} }
        token = tok
        params["access_token"] = token
    }

    // 准备签名路径
    signPath := fmt.Sprintf("param2/%s/%s", api, c.appKey)

    // 从参数中剔除 multipart 键
    mpKeys := req.MultipartParams()
    paramsForSign := make(map[string]string)
    normParams := make(map[string]string)
    for k, v := range params {
        // 忽略空值：与 Python 版 _get_nonnull_biz_params 保持一致（此处简单判空）
        if v == nil { continue }
        sv := toString(v)
        normParams[k] = sv
    }
    for k, v := range normParams {
        if slices.Contains(mpKeys, k) { continue }
        paramsForSign[k] = v
    }

    // 计算签名
    var siHash string
    if req.NeedSign() {
        if c.appKey == "" || c.secret == "" {
            return &AopError{Kind: "sign", Message: "appKey/secret missing", APIURI: api}
        }
        signInput := buildSignInput(signPath, paramsForSign)
        siHash = hashHexSHA1(signInput)
        signature := Sign(c.secret, signInput)
        normParams["_aop_signature"] = signature
    }

    // URL 拼装
    scheme := "http"
    if req.NeedHTTPS() { scheme = "https" }
    root := "openapi"
    if req.IsInnerAPI() { root = "api" }
    urlStr := fmt.Sprintf("%s://%s/%s/%s", scheme, c.server, root, signPath)

    // 头
    headers := make(http.Header)
    headers.Set("Cache-Control", "no-cache")
    headers.Set("Connection", "Keep-Alive")
    headers.Set("User-Agent", c.userAgent)
    // 可选：注入 request-id（从 ctx 读取）
    if rid := requestIDFromCtx(ctx); rid != "" { headers.Set("X-Client-Request-Id", rid) }

    // 文件映射
    files := map[string]FileItem{}
    for _, k := range mpKeys {
        if v, ok := params[k]; ok {
            if fi, ok := v.(FileItem); ok {
                files[k] = fi
                delete(normParams, k)
            }
        }
    }

    // 日志：BeforeRequest（仅记录键）
    c.logger.Info(ctx, "request.begin",
        Field{Key: "api_uri", Value: api},
        Field{Key: "host", Value: c.server},
        Field{Key: "path", Value: signPath},
        Field{Key: "need_sign", Value: req.NeedSign()},
        Field{Key: "need_ts", Value: req.NeedTimestamp()},
        Field{Key: "need_auth", Value: req.NeedAuth()},
        Field{Key: "param_keys", Value: keysOf(normParams)},
        Field{Key: "multipart_keys", Value: mpKeys},
        Field{Key: "sign_input_sha1", Value: siHash},
    )

    // 发送
    start := time.Now()
    status, preview, err := c.transport(ctx, http.MethodPost, urlStr, headers, normParams, files, out)
    dur := time.Since(start)

    // 响应日志
    if err != nil {
        // ApiError 或 AopError
        fields := []Field{
            {Key: "api_uri", Value: api},
            {Key: "status", Value: status},
            {Key: "preview", Value: previewIf(c, preview)},
        }
        switch e := err.(type) {
        case *ApiError:
            fields = append(fields,
                Field{Key: "error_code", Value: e.ErrorCode},
                Field{Key: "error_message", Value: e.ErrorMsg},
                Field{Key: "exception", Value: e.Exception},
                Field{Key: "server_request_id", Value: e.RequestID},
            )
        case *AopError:
            fields = append(fields,
                Field{Key: "error_kind", Value: e.Kind},
                Field{Key: "message", Value: e.Message},
            )
        default:
            fields = append(fields, Field{Key: "error", Value: err.Error()})
        }
        c.logger.Error(ctx, "request.error", fields...)
        return err
    }

    c.logger.Info(ctx, "request.ok",
        Field{Key: "api_uri", Value: api},
        Field{Key: "status", Value: status},
        Field{Key: "preview", Value: previewIfOnSuccess(c, preview)},
        Field{Key: "duration_ms", Value: dur.Milliseconds()},
    )
    return nil
}

func toString(v any) string {
    switch t := v.(type) {
    case string:
        return t
    case fmt.Stringer:
        return t.String()
    default:
        return fmt.Sprint(v)
    }
}

func missingKeys(params map[string]any, required []string) []string {
    var miss []string
    for _, k := range required {
        if _, ok := params[k]; !ok {
            miss = append(miss, k)
        }
    }
    return miss
}

func keysOf(m map[string]string) []string {
    ks := make([]string, 0, len(m))
    for k := range m { ks = append(ks, k) }
    slices.Sort(ks)
    return ks
}

// 预览策略：错误时一定输出，成功时根据配置
func previewIf(c *Client, s string) string {
    if c.redact.BodyOnErrorOnly { return s }
    return s
}
func previewIfOnSuccess(c *Client, s string) string {
    if c.redact.BodyOnErrorOnly { return "" }
    return s
}

// request-id 提供：从 context 读取 key，用户可自行注入
type ctxKey string

const requestIDKey ctxKey = "request-id"

func WithRequestID(ctx context.Context, id string) context.Context { return context.WithValue(ctx, requestIDKey, id) }
func requestIDFromCtx(ctx context.Context) string {
    v := ctx.Value(requestIDKey)
    if v == nil { return "" }
    if s, ok := v.(string); ok { return s }
    return ""
}

// AccessTokenProvider token 提供者接口
type AccessTokenProvider interface {
    Token(ctx context.Context) (string, error)
}

// StaticToken 固定 token 提供者
type StaticToken string

func (s StaticToken) Token(_ context.Context) (string, error) { return string(s), nil }

// urlJoin 安全拼装（备用）
func urlJoin(base, p string) string {
    u, err := url.Parse(base)
    if err != nil { return strings.TrimRight(base, "/") + "/" + strings.TrimLeft(p, "/") }
    u.Path = strings.TrimRight(u.Path, "/") + "/" + strings.TrimLeft(p, "/")
    return u.String()
}

// hashHexSHA1 计算十六进制小写 SHA1
func hashHexSHA1(b []byte) string {
    h := sha1.Sum(b)
    return hex.EncodeToString(h[:])
}
