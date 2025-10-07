package biz

import (
    "io/fs"
    "os"
    "path/filepath"
    "regexp"
    "strings"
)

// RegisterFromPython 解析 aop Python SDK 的 biz 目录，构建并注册所有 API 描述。
// dir 参数应指向 aop/api/biz 目录。
// 解析采用简单正则，适配当前仓库中的模板代码风格。
func RegisterFromPython(dir string) error {
    // 正则：类名、uri、布尔开关、必填与 multipart 列表
    reClass := regexp.MustCompile(`class\s+(\w+)\(BaseApi\):`)
    reURI := regexp.MustCompile(`def\s+get_api_uri\(self\):\s*\n\s*return\s+["']([^"']+)["']`)
    reBool := func(name string) *regexp.Regexp {
        return regexp.MustCompile(`def\s+`+name+`\(self\):\s*\n\s*return\s+(True|False)`) }
    reReq := regexp.MustCompile(`def\s+get_required_params\(self\):\s*\n\s*return\s*\[(?s:(.*?))\]`)
    reMP := regexp.MustCompile(`def\s+get_multipart_params\(self\):\s*\n\s*return\s*\[(?s:(.*?))\]`)

    needSign := reBool("need_sign")
    needTs := reBool("need_timestamp")
    needAuth := reBool("need_auth")
    needHTTPS := reBool("need_https")
    isInner := reBool("is_inner_api")

    parseList := func(s string) []string {
        s = strings.TrimSpace(s)
        if s == "" { return nil }
        // 逗号分隔，去引号与空白
        parts := strings.Split(s, ",")
        out := make([]string, 0, len(parts))
        for _, p := range parts {
            p = strings.TrimSpace(p)
            if p == "" { continue }
            if (strings.HasPrefix(p, "\"") && strings.HasSuffix(p, "\"")) || (strings.HasPrefix(p, "'") && strings.HasSuffix(p, "'")) {
                p = p[1:len(p)-1]
            }
            out = append(out, p)
        }
        return out
    }

    walkFn := func(path string, d fs.DirEntry, err error) error {
        if err != nil { return err }
        if d.IsDir() || !strings.HasSuffix(strings.ToLower(d.Name()), ".py") { return nil }
        b, err := os.ReadFile(path)
        if err != nil { return err }
        txt := string(b)
        mc := reClass.FindStringSubmatch(txt)
        mu := reURI.FindStringSubmatch(txt)
        if mc == nil || mu == nil { return nil }
        name := mc[1]
        if strings.HasSuffix(name, "Param") { name = name[:len(name)-5] }
        uri := mu[1]
        bSign := needSign.FindStringSubmatch(txt)
        bTs := needTs.FindStringSubmatch(txt)
        bAuth := needAuth.FindStringSubmatch(txt)
        bHTTPS := needHTTPS.FindStringSubmatch(txt)
        bInner := isInner.FindStringSubmatch(txt)
        req := reReq.FindStringSubmatch(txt)
        mp := reMP.FindStringSubmatch(txt)
        dsc := Descriptor{
            Name:         name,
            APIURI:       uri,
            NeedSign:     bSign != nil && bSign[1] == "True",
            NeedTimestamp: bTs != nil && bTs[1] == "True",
            NeedAuth:     bAuth != nil && bAuth[1] == "True",
            NeedHTTPS:    bHTTPS != nil && bHTTPS[1] == "True",
            IsInnerAPI:   bInner != nil && bInner[1] == "True",
            Required:     nil,
            Multipart:    nil,
        }
        if req != nil { dsc.Required = parseList(req[1]) }
        if mp != nil { dsc.Multipart = parseList(mp[1]) }
        Register(dsc)
        return nil
    }

    return filepath.WalkDir(dir, walkFn)
}

