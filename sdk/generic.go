package sdk

// GenericRequest 通用请求封装，便于批量生成 API 包装函数。
// 业务参数通过 ParamsMap 传入；必填参数通过 Required 指定；
// 其余钩子由布尔字段控制，满足 APIRequest 接口。
type GenericRequest struct {
    BaseRequest

    APIURI    string
    Sign      bool
    Timestamp bool
    Auth      bool
    HTTPS     bool
    Inner     bool

    Required  []string
    Multipart []string
    ParamsMap map[string]any
}

func (g *GenericRequest) API() APIInfo             { return APIInfo{URI: g.APIURI} }
func (g *GenericRequest) NeedSign() bool           { return g.Sign }
func (g *GenericRequest) NeedTimestamp() bool      { return g.Timestamp }
func (g *GenericRequest) NeedAuth() bool           { return g.Auth }
func (g *GenericRequest) NeedHTTPS() bool          { return g.HTTPS }
func (g *GenericRequest) IsInnerAPI() bool         { return g.Inner }
func (g *GenericRequest) RequiredParams() []string { return g.Required }
func (g *GenericRequest) MultipartParams() []string { return g.Multipart }
func (g *GenericRequest) Params() map[string]any   { return g.ParamsMap }

