package sdk

import "maps"

// APIInfo 描述一个 API 的唯一标识（用于 URL 与签名）
type APIInfo struct {
    // URI 形如: "1/system/currentTimeMillis"
    URI string
}

// APIRequest 定义 API 请求必须实现的接口。
// Client.Do 会基于这些钩子完成模板化的调用流程。
type APIRequest interface {
    // API 返回 version/namespace/name
    API() APIInfo

    // NeedSign 是否需要签名
    NeedSign() bool
    // NeedTimestamp 是否需要 _aop_timestamp
    NeedTimestamp() bool
    // NeedAuth 是否需要 access_token
    NeedAuth() bool
    // NeedHTTPS 是否使用 https 协议
    NeedHTTPS() bool
    // IsInnerAPI 是否为内部 API（路径使用 /api 而非 /openapi）
    IsInnerAPI() bool

    // MultipartParams 返回需要作为文件上传的参数键列表
    MultipartParams() []string
    // RequiredParams 返回业务必填参数名（不含系统参数）
    RequiredParams() []string
    // Params 返回业务参数（不含系统参数，也不包含 Multipart 内容）
    Params() map[string]any
}

// BaseRequest 提供默认实现，业务请求可通过匿名字段嵌入后覆盖需要的钩子。
type BaseRequest struct{}

func (BaseRequest) NeedSign() bool          { return false }
func (BaseRequest) NeedTimestamp() bool     { return false }
func (BaseRequest) NeedAuth() bool          { return false }
func (BaseRequest) NeedHTTPS() bool         { return false }
func (BaseRequest) IsInnerAPI() bool        { return false }
func (BaseRequest) MultipartParams() []string { return nil }
func (BaseRequest) RequiredParams() []string  { return nil }
func (BaseRequest) Params() map[string]any    { return map[string]any{} }

// copyParams 用于复制 map，避免被外部修改。
func copyParams(src map[string]any) map[string]any {
    if src == nil {
        return map[string]any{}
    }
    // Go1.21+ 提供 maps.Clone
    return maps.Clone(src)
}

