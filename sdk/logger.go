package sdk

import (
    "context"
)

// LogLevel 日志级别
type LogLevel int

const (
    DebugLevel LogLevel = iota
    InfoLevel
    WarnLevel
    ErrorLevel
)

// Field 结构化字段
type Field struct {
    Key   string
    Value any
}

// Logger 抽象日志接口，便于接入不同日志库。
type Logger interface {
    Debug(ctx context.Context, msg string, fields ...Field)
    Info(ctx context.Context, msg string, fields ...Field)
    Warn(ctx context.Context, msg string, fields ...Field)
    Error(ctx context.Context, msg string, fields ...Field)
}

// RedactConfig 脱敏配置
type RedactConfig struct {
    // 是否记录业务参数的值，默认仅记录键名
    LogParamValues bool
    // 响应体预览的最大字节数
    MaxBodyPreview int
    // 仅在错误时记录 Body 预览
    BodyOnErrorOnly bool
}

// defaultRedact 默认脱敏配置
func defaultRedact() RedactConfig {
    return RedactConfig{
        LogParamValues: false,
        MaxBodyPreview: 2048,
        BodyOnErrorOnly: true,
    }
}

// NopLogger 空实现
type NopLogger struct{}

func (NopLogger) Debug(ctx context.Context, msg string, fields ...Field) {}
func (NopLogger) Info(ctx context.Context, msg string, fields ...Field)  {}
func (NopLogger) Warn(ctx context.Context, msg string, fields ...Field)  {}
func (NopLogger) Error(ctx context.Context, msg string, fields ...Field) {}

