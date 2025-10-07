package sdk

import (
    "context"
    "log/slog"
)

// SlogAdapter 适配标准库 slog
type SlogAdapter struct {
    l *slog.Logger
}

func NewSlogAdapter(l *slog.Logger) *SlogAdapter { return &SlogAdapter{l: l} }

func (s *SlogAdapter) Debug(ctx context.Context, msg string, fields ...Field) {
    s.l.Log(ctx, slog.LevelDebug, msg, toAttrs(fields)...)
}
func (s *SlogAdapter) Info(ctx context.Context, msg string, fields ...Field) {
    s.l.Log(ctx, slog.LevelInfo, msg, toAttrs(fields)...)
}
func (s *SlogAdapter) Warn(ctx context.Context, msg string, fields ...Field) {
    s.l.Log(ctx, slog.LevelWarn, msg, toAttrs(fields)...)
}
func (s *SlogAdapter) Error(ctx context.Context, msg string, fields ...Field) {
    s.l.Log(ctx, slog.LevelError, msg, toAttrs(fields)...)
}

func toAttrs(fields []Field) []any {
    if len(fields) == 0 {
        return nil
    }
    attrs := make([]any, 0, len(fields)*2)
    for _, f := range fields {
        attrs = append(attrs, f.Key, f.Value)
    }
    return attrs
}

