package common

import "github.com/yuuzao/1688-go-sdk/sdk"

// AuthGetTokenRequest 获取 access_token（参考 1688 授权 API 文档）。
// 这里只定义骨架与典型参数字段，调用方可根据授权模式（授权码/刷新）设置。
// API: 1/system.oauth2/getToken
type AuthGetTokenRequest struct {
    sdk.BaseRequest

    // 典型字段（按需使用）：grant_type, code, refresh_token, redirect_uri 等
    ParamsMap map[string]any
}

func NewAuthGetToken() *AuthGetTokenRequest { return &AuthGetTokenRequest{ParamsMap: map[string]any{}} }

func (r *AuthGetTokenRequest) API() sdk.APIInfo     { return sdk.APIInfo{URI: "1/system.oauth2/getToken"} }
func (r *AuthGetTokenRequest) NeedSign() bool       { return false }
func (r *AuthGetTokenRequest) NeedTimestamp() bool  { return false }
func (r *AuthGetTokenRequest) NeedAuth() bool       { return false }
func (r *AuthGetTokenRequest) NeedHTTPS() bool      { return true }
func (r *AuthGetTokenRequest) IsInnerAPI() bool     { return false }
func (r *AuthGetTokenRequest) Params() map[string]any { return r.ParamsMap }

// AuthGetTokenResponse 示例响应结构，实际字段以文档为准
type AuthGetTokenResponse struct {
    AccessToken  string `json:"access_token"`
    RefreshToken string `json:"refresh_token"`
    ExpiresIn    int64  `json:"expires_in"`
}
