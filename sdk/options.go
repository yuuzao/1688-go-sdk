package sdk

import (
    "log/slog"
    "sync/atomic"
    "time"
)

// Option 函数式选项
type Option func(*Client)

// WithServer 设置远端域名（例如 gw.open.1688.com 或 127.0.0.1:port，用作 Host）
func WithServer(server string) Option { return func(c *Client) { c.server = server } }

// WithAppInfo 设置 appKey 与 secret
func WithAppInfo(appKey, secret string) Option { return func(c *Client) { c.appKey, c.secret = appKey, secret } }

// WithHTTPClient 替换默认 HTTP 客户端
func WithHTTPClient(hc Doer) Option { return func(c *Client) { c.http = hc } }

// WithLogger 注入日志实现
func WithLogger(l Logger) Option { return func(c *Client) { c.logger = l } }

// WithSlog 便捷注入 slog
func WithSlog(l *slog.Logger) Option { return WithLogger(NewSlogAdapter(l)) }

// WithLogLevel 设置日志等级（保留接口，当前内部未按级别过滤）
func WithLogLevel(_ LogLevel) Option { return func(c *Client) {} }

// WithTimestampSource 设置时间戳策略
func WithTimestampSource(src TimestampSource) Option { return func(c *Client) { c.tsSource = src } }

// WithTokenProvider 设置 token 提供者
func WithTokenProvider(p AccessTokenProvider) Option { return func(c *Client) { c.tokenProvider = p } }

// WithUserAgent 自定义 UA
func WithUserAgent(ua string) Option { return func(c *Client) { c.userAgent = ua } }

// WithTimeout 设置请求超时
func WithTimeout(d time.Duration) Option { return func(c *Client) { c.timeout.Store(d) } }

// WithRedact 配置脱敏策略
func WithRedact(cfg RedactConfig) Option { return func(c *Client) { c.redact = cfg } }

// helper 读取超时
func (c *Client) timeoutValue() time.Duration {
    if v := c.timeout.Load(); v != nil {
        return v.(time.Duration)
    }
    return 30 * time.Second
}

// atomicDuration 为 time.Duration 提供原子读写
type atomicDuration struct{ v atomic.Value }

func (a *atomicDuration) Store(d time.Duration) { a.v.Store(d) }
func (a *atomicDuration) Load() any             { return a.v.Load() }

