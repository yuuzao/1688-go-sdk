package sdk

import (
    "context"
    "io"
    "net/http"
    "net/http/httptest"
    "net/url"
    "strings"
    "testing"
)

// dummy request implementing APIRequest
type signTestReq struct{ BaseRequest }
func (signTestReq) API() APIInfo                { return APIInfo{URI: "1/test/echo"} }
func (signTestReq) NeedSign() bool              { return true }
func (signTestReq) NeedTimestamp() bool         { return true }
func (signTestReq) NeedAuth() bool              { return true }
func (signTestReq) Params() map[string]any      { return map[string]any{"foo": "bar"} }

func TestClient_Do_SignAndURL(t *testing.T) {
    // fake server 校验路径与签名
    secret := "sec"; appKey := "ak"
    var capturedPath string
    svr := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        capturedPath = r.URL.Path
        // 解析 form
        _ = r.ParseMultipartForm(10 << 20)
        if r.Header.Get("Content-Type") == "application/x-www-form-urlencoded" {
            // ok
        }
        // 收集参数用于校验签名（排除 multipart）
        vals := r.PostForm
        gotSign := vals.Get("_aop_signature")
        vals.Del("_aop_signature")
        // 构造 paramsForSign
        params := map[string]string{}
        for k := range vals { params[k] = vals.Get(k) }
        signPath := "param2/1/test/echo/" + appKey
        want := Sign(secret, buildSignInput(signPath, params))
        if gotSign != want {
            http.Error(w, `{"error_code":"SIG","error_message":"bad sign"}`, 400)
            return
        }
        io.WriteString(w, `{"ok":true}`)
    }))
    defer svr.Close()

    host := mustHost(svr.URL)
    cli := NewClient(
        WithServer(host),
        WithAppInfo(appKey, secret),
        WithTokenProvider(StaticToken("tkn")),
        WithTimestampSource(LocalClock()),
    )

    var resp map[string]any
    if err := cli.Do(context.Background(), signTestReq{}, &resp); err != nil {
        t.Fatalf("Do error: %v", err)
    }
    if capturedPath != "/openapi/param2/1/test/echo/ak" {
        t.Fatalf("path mismatch: %s", capturedPath)
    }
}

type mpReq struct{ BaseRequest }
func (mpReq) API() APIInfo                    { return APIInfo{URI: "1/test/upload"} }
func (mpReq) NeedSign() bool                  { return true }
func (mpReq) MultipartParams() []string       { return []string{"image"} }
func (mpReq) Params() map[string]any          { return map[string]any{"name":"n", "image": FileItem{Name:"a.txt", Content: strings.NewReader("hello")}} }

func TestClient_Do_MultipartExclusion(t *testing.T) {
    secret := "sec"; appKey := "ak"
    svr := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        // 必须是 multipart
        if !strings.HasPrefix(r.Header.Get("Content-Type"), "multipart/") {
            http.Error(w, `{"error_code":"CT","error_message":"not multipart"}`, 400)
            return
        }
        // 读取 multipart
        mr, err := r.MultipartReader()
        if err != nil { t.Fatal(err) }
        params := map[string]string{}
        var hasFile bool
        for {
            part, err := mr.NextPart()
            if err == io.EOF { break }
            if err != nil { t.Fatal(err) }
            buf, _ := io.ReadAll(part)
            cd := part.Header.Get("Content-Disposition")
            if strings.Contains(cd, "filename=") { hasFile = true }
            name := part.FormName()
            if name == "image" { continue } // 不参与签名
            params[name] = string(buf)
        }
        if !hasFile { t.Fatal("no file part") }
        signPath := "param2/1/test/upload/" + appKey
        got := params["_aop_signature"]; delete(params, "_aop_signature")
        want := Sign(secret, buildSignInput(signPath, params))
        if got != want { t.Fatalf("bad sign: %s != %s", got, want) }
        io.WriteString(w, `{"ok":true}`)
    }))
    defer svr.Close()

    host := mustHost(svr.URL)
    cli := NewClient(WithServer(host), WithAppInfo(appKey, secret))
    var resp map[string]any
    if err := cli.Do(context.Background(), mpReq{}, &resp); err != nil {
        t.Fatalf("Do error: %v", err)
    }
}

func TestClient_Do_ErrorDecoding(t *testing.T) {
    svr := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        http.Error(w, `{"error_code":"E1","error_message":"bad","exception":"ex","request_id":"rq"}`, 400)
    }))
    defer svr.Close()
    host := mustHost(svr.URL)
    cli := NewClient(WithServer(host))
    var out map[string]any
    err := cli.Do(context.Background(), &GetServerTimeEcho{}, &out)
    if err == nil { t.Fatal("expected error") }
    if !IsApiError(err) { t.Fatalf("want ApiError, got %T", err) }
    ae := err.(*ApiError)
    if ae.ErrorCode != "E1" || ae.RequestID != "rq" { t.Fatalf("unexpected api error: %+v", ae) }
}

func TestClient_Do_JSONParseError(t *testing.T) {
    svr := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(200)
        io.WriteString(w, "not-json")
    }))
    defer svr.Close()
    host := mustHost(svr.URL)
    cli := NewClient(WithServer(host))
    var out map[string]any
    err := cli.Do(context.Background(), &GetServerTimeEcho{}, &out)
    if err == nil { t.Fatal("expected error") }
    if !IsAopError(err) { t.Fatalf("want AopError, got %T", err) }
}

// 支持测试的简单 request：返回 JSON 对象
type GetServerTimeEcho struct{ BaseRequest }
func (GetServerTimeEcho) API() APIInfo { return APIInfo{URI: "1/system/currentTimeMillis"} }

func TestCommon_GetServerTimestamp_Number(t *testing.T) {
    svr := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(200)
        io.WriteString(w, "12345") // 纯数字 JSON
    }))
    defer svr.Close()
    host := mustHost(svr.URL)
    cli := NewClient(WithServer(host))
    var out int64
    if err := cli.Do(context.Background(), &GetServerTimeEcho{}, &out); err != nil {
        t.Fatalf("Do error: %v", err)
    }
    if out != 12345 { t.Fatalf("unexpected: %d", out) }
}

func mustHost(raw string) string {
    u, _ := url.Parse(raw)
    return u.Host
}
