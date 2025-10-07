package sdk

import (
    "errors"
    "fmt"
)

// AopError 表示在发送请求前或解析响应时出现的本地错误。
// 场景示例：
// 1) 必填参数缺失；2) JSON 解析失败；3) 网络/超时等异常。
type AopError struct {
    Kind      string // net/json/param/sign/timeout/other
    Message   string
    Status    int
    RequestID string
    APIURI    string
}

func (e *AopError) Error() string {
    return fmt.Sprintf("AopError[kind=%s, api=%s, status=%d, req_id=%s] %s", e.Kind, e.APIURI, e.Status, e.RequestID, e.Message)
}

// ApiError 表示远端服务返回了明确的错误，并成功被解析。
type ApiError struct {
    API         string
    ErrorCode   string
    ErrorMsg    string
    Exception   string
    RequestID   string
    HTTPStatus  int
}

func (e *ApiError) Error() string {
    return fmt.Sprintf("ApiError[api=%s; error_code=%s; error_message=%s; exception=%s; request_id=%s]", e.API, e.ErrorCode, e.ErrorMsg, e.Exception, e.RequestID)
}

// IsApiError 便于调用方判断错误类型。
func IsApiError(err error) bool {
    var ae *ApiError
    return errors.As(err, &ae)
}

// IsAopError 便于调用方判断错误类型。
func IsAopError(err error) bool {
    var ae *AopError
    return errors.As(err, &ae)
}

