package sdk

import (
    "crypto/hmac"
    "crypto/sha1"
    "encoding/hex"
    "sort"
    "strings"
)

// buildSignInput 根据 Python 版规则拼接签名输入：signPath + 按键名排序的 k+v 拼接。
func buildSignInput(signPath string, params map[string]string) []byte {
    keys := make([]string, 0, len(params))
    for k := range params {
        keys = append(keys, k)
    }
    sort.Strings(keys)

    var b strings.Builder
    b.WriteString(signPath)
    for _, k := range keys {
        b.WriteString(k)
        b.WriteString(params[k])
    }
    return []byte(b.String())
}

// Sign 计算 HMAC-SHA1 并以大写十六进制返回。
func Sign(secret string, signInput []byte) string {
    mac := hmac.New(sha1.New, []byte(secret))
    mac.Write(signInput)
    sum := mac.Sum(nil)
    s := strings.ToUpper(hex.EncodeToString(sum))
    return s
}

