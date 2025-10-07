package common

import "github.com/yuuzao/1688-go-sdk/sdk"

// GetServerTimestampRequest 获取服务器时间戳（毫秒）
// API: 1/system/currentTimeMillis
type GetServerTimestampRequest struct{ sdk.BaseRequest }

func NewGetServerTimestamp() *GetServerTimestampRequest { return &GetServerTimestampRequest{} }

func (r *GetServerTimestampRequest) API() sdk.APIInfo { return sdk.APIInfo{URI: "1/system/currentTimeMillis"} }
func (r *GetServerTimestampRequest) NeedSign() bool      { return false }
func (r *GetServerTimestampRequest) NeedTimestamp() bool { return false }
func (r *GetServerTimestampRequest) NeedAuth() bool      { return false }
func (r *GetServerTimestampRequest) NeedHTTPS() bool     { return false }
func (r *GetServerTimestampRequest) IsInnerAPI() bool    { return false }
func (r *GetServerTimestampRequest) Params() map[string]any { return map[string]any{} }
