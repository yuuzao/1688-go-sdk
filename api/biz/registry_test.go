package biz

import "testing"

// 静态注册表测试：校验典型条目与映射完整性
func TestStaticRegistryLoaded(t *testing.T) {
    // registry_static.go 的 init() 会在包初始化时注册所有 API
    d, ok := RegistryByName["AlibabaProductGet"]
    if !ok { t.Fatalf("AlibabaProductGet not found in static registry") }
    if !d.NeedSign || !d.NeedAuth || d.NeedTimestamp || d.NeedHTTPS || d.IsInnerAPI {
        t.Fatalf("flags mismatch: %+v", d)
    }
    if len(d.Required) == 0 { t.Fatalf("required list empty") }

    if _, ok := RegistryByURI[d.APIURI]; !ok {
        t.Fatalf("URI lookup failed for %s", d.APIURI)
    }

    r := New("AlibabaProductGet")
    if r == nil { t.Fatalf("New returned nil") }
}
