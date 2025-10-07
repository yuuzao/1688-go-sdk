package biz

import (
    "github.com/yuuzao/1688-go-sdk/sdk"
)

// Descriptor 描述一个 API 的元信息（来源于 Python SDK 的请求类定义）。
// 为了降低维护成本，默认通过 RegisterFromPython 在构建/测试阶段从 aop 目录解析生成。
// 发布为独立模块时，可以把生成结果固化为静态表。
type Descriptor struct {
    Name         string   // 例如 AlibabaProductGet
    APIURI       string   // 例如 1/com.alibaba.product/alibaba.product.get
    NeedSign     bool
    NeedTimestamp bool
    NeedAuth     bool
    NeedHTTPS    bool
    IsInnerAPI   bool
    Required     []string
    Multipart    []string
}

var (
    // RegistryByName 以类名注册（推荐）
    RegistryByName = map[string]Descriptor{}
    // RegistryByURI 以 APIURI 注册（便于按文档直接使用）
    RegistryByURI  = map[string]Descriptor{}
)

// Register 将描述信息加入注册表（重复名将覆盖）。
func Register(d Descriptor) {
    RegistryByName[d.Name] = d
    RegistryByURI[d.APIURI] = d
}

// New 基于注册名创建通用请求。
func New(name string) *sdk.GenericRequest {
    d, ok := RegistryByName[name]
    if !ok { return nil }
    return &sdk.GenericRequest{
        APIURI:    d.APIURI,
        Sign:      d.NeedSign,
        Timestamp: d.NeedTimestamp,
        Auth:      d.NeedAuth,
        HTTPS:     d.NeedHTTPS,
        Inner:     d.IsInnerAPI,
        Required:  append([]string(nil), d.Required...),
        Multipart: append([]string(nil), d.Multipart...),
        ParamsMap: map[string]any{},
    }
}

// NewByURI 基于 APIURI 创建通用请求。
func NewByURI(uri string) *sdk.GenericRequest {
    d, ok := RegistryByURI[uri]
    if !ok { return nil }
    return &sdk.GenericRequest{
        APIURI:    d.APIURI,
        Sign:      d.NeedSign,
        Timestamp: d.NeedTimestamp,
        Auth:      d.NeedAuth,
        HTTPS:     d.NeedHTTPS,
        Inner:     d.IsInnerAPI,
        Required:  append([]string(nil), d.Required...),
        Multipart: append([]string(nil), d.Multipart...),
        ParamsMap: map[string]any{},
    }
}
