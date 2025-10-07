package common

import "github.com/yuuzao/1688-go-sdk/sdk"

// AuthPostponeTokenRequest 延长 access_token 有效期。
// API: 1/system.oauth2/postponeToken
type AuthPostponeTokenRequest struct {
    sdk.BaseRequest
    ParamsMap map[string]any
}

func NewAuthPostponeToken() *AuthPostponeTokenRequest { return &AuthPostponeTokenRequest{ParamsMap: map[string]any{}} }

func (r *AuthPostponeTokenRequest) API() sdk.APIInfo     { return sdk.APIInfo{URI: "1/system.oauth2/postponeToken"} }
func (r *AuthPostponeTokenRequest) NeedSign() bool       { return false }
func (r *AuthPostponeTokenRequest) NeedTimestamp() bool  { return false }
func (r *AuthPostponeTokenRequest) NeedAuth() bool       { return true }
func (r *AuthPostponeTokenRequest) NeedHTTPS() bool      { return true }
func (r *AuthPostponeTokenRequest) IsInnerAPI() bool     { return false }
func (r *AuthPostponeTokenRequest) Params() map[string]any { return r.ParamsMap }

type AuthPostponeTokenResponse struct {
    AccessToken  string `json:"access_token"`
    ExpiresIn    int64  `json:"expires_in"`
}
