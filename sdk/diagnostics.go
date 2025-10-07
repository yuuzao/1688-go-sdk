package sdk

import (
    "encoding/json"
    "fmt"
    "sort"
    "strings"
)

// Repro 摘要（脱敏），便于问题复现与排障
type Repro struct {
    Host        string   `json:"host"`
    APIURI      string   `json:"api_uri"`
    IsInner     bool     `json:"is_inner_api"`
    NeedHTTPS   bool     `json:"need_https"`
    ParamKeys   []string `json:"param_keys"`
    SignPath    string   `json:"sign_path"`
    SignatureID string   `json:"sign_input_sha1"`
}

func (r Repro) String() string { b, _ := json.Marshal(r); return string(b) }

// MaskToken 对 token 脱敏显示
func MaskToken(s string) string {
    if s == "" { return s }
    if len(s) <= 6 { return "***" }
    return s[:3] + "***" + s[len(s)-3:]
}

// Curl 生成一个近似的 curl 命令（敏感值使用占位符）
func Curl(url string, params map[string]string) string {
    // 将参数以 -d 形式输出
    keys := make([]string, 0, len(params))
    for k := range params { keys = append(keys, k) }
    sort.Strings(keys)
    var parts []string
    for _, k := range keys {
        v := params[k]
        if strings.Contains(strings.ToLower(k), "secret") || strings.Contains(strings.ToLower(k), "token") {
            v = "<REDACTED>"
        }
        parts = append(parts, fmt.Sprintf("-d '%s=%s'", k, v))
    }
    return fmt.Sprintf("curl -X POST '%s' %s", url, strings.Join(parts, " "))
}

