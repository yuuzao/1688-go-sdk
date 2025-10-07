package sdk

import (
    "bytes"
    "context"
    "encoding/json"
    "fmt"
    "io"
    "mime/multipart"
    "net/http"
    "net/url"
    "strings"
    "time"
)

// Doer 用于替换 http.Client，方便测试与注入。
type Doer interface {
    Do(req *http.Request) (*http.Response, error)
}

// transport 封装发送请求与响应解码。
func (c *Client) transport(ctx context.Context, method, urlStr string, headers http.Header, params map[string]string, files map[string]FileItem, out any) (status int, bodyPreview string, err error) {
    var req *http.Request
    var contentType string

    // 选择 form 或 multipart
    if len(files) > 0 {
        var buf bytes.Buffer
        mw := multipart.NewWriter(&buf)
        for k, v := range params {
            _ = mw.WriteField(k, v)
        }
        for k, f := range files {
            fw, e := mw.CreateFormFile(k, f.Name)
            if e != nil {
                return 0, "", e
            }
            if f.Content != nil {
                if _, e = io.Copy(fw, f.Content); e != nil {
                    return 0, "", e
                }
            }
        }
        _ = mw.Close()
        contentType = mw.FormDataContentType()
        r, e := http.NewRequestWithContext(ctx, method, urlStr, &buf)
        if e != nil { return 0, "", e }
        req = r
    } else {
        form := url.Values{}
        for k, v := range params { form.Set(k, v) }
        body := strings.NewReader(form.Encode())
        r, e := http.NewRequestWithContext(ctx, method, urlStr, body)
        if e != nil { return 0, "", e }
        contentType = "application/x-www-form-urlencoded"
        req = r
    }

    for k, vs := range headers { for _, v := range vs { req.Header.Add(k, v) } }
    if contentType != "" { req.Header.Set("Content-Type", contentType) }

    // 发送
    start := time.Now()
    resp, e := c.http.Do(req)
    dur := time.Since(start)
    if e != nil {
        return 0, "", &AopError{Kind: "net", Message: e.Error(), RequestID: requestIDFromCtx(ctx), APIURI: urlStr}
    }
    defer resp.Body.Close()
    status = resp.StatusCode

    // 读取 body（限制预览长度）
    // 实际解码仍然基于 json.Decoder，从 buf 中读取
    raw, _ := io.ReadAll(resp.Body)
    preview := raw
    max := c.redact.MaxBodyPreview
    if max <= 0 { max = 2048 }
    if len(preview) > max { preview = preview[:max] }
    bodyPreview = string(preview)

    // 日志（成功/失败）在外层 Do 进行，这里只做解析
    // 尝试 JSON 解码
    if status < 200 || status >= 400 {
        // 先尝试解析错误结构
        var m map[string]any
        if err := json.Unmarshal(raw, &m); err == nil {
            ae := &ApiError{
                API:        "",
                ErrorCode:  strFromAny(m["error_code"]),
                ErrorMsg:   strFromAny(m["error_message"]),
                Exception:  strFromAny(m["exception"]),
                RequestID:  strFromAny(m["request_id"]),
                HTTPStatus: status,
            }
            return status, bodyPreview, ae
        }
        return status, bodyPreview, &AopError{Kind: "http", Message: fmt.Sprintf("status=%d", status), Status: status, RequestID: requestIDFromCtx(ctx)}
    }

    if out == nil {
        return status, bodyPreview, nil
    }

    if err := json.Unmarshal(raw, out); err != nil {
        return status, bodyPreview, &AopError{Kind: "json", Message: err.Error(), Status: status, RequestID: requestIDFromCtx(ctx)}
    }
    // 打点耗时（在 Do 内部日志输出）
    _ = dur
    return status, bodyPreview, nil
}

func strFromAny(v any) string {
    switch t := v.(type) {
    case string:
        return t
    case fmt.Stringer:
        return t.String()
    case float64:
        // 避免科学计数，尽量整洁
        return strings.TrimRight(strings.TrimRight(fmt.Sprintf("%f", t), "0"), ".")
    default:
        if v == nil { return "" }
        b, _ := json.Marshal(v)
        return string(b)
    }
}

