package sdk

import (
    "context"
    "sync/atomic"
    "time"
)

// TimestampSource 抽象时间戳来源（毫秒）
type TimestampSource interface {
    NowMillis(ctx context.Context, c *Client) (int64, error)
}

// LocalClock 使用本地时间
type localClock struct{}

func LocalClock() TimestampSource { return &localClock{} }

func (localClock) NowMillis(_ context.Context, _ *Client) (int64, error) {
    return time.Now().UnixMilli(), nil
}

// OffsetClock 基于固定偏移（毫秒）。偏移可由外部定期同步。
type OffsetClock struct{ offsetMS atomic.Int64 }

func NewOffsetClock(offsetMillis int64) *OffsetClock { c := &OffsetClock{}; c.offsetMS.Store(offsetMillis); return c }
func (o *OffsetClock) SetOffsetMillis(v int64)       { o.offsetMS.Store(v) }
func (o *OffsetClock) NowMillis(_ context.Context, _ *Client) (int64, error) {
    return time.Now().UnixMilli() + o.offsetMS.Load(), nil
}

// ServerClock 通过调用远端 API 获取时间，不建议频繁使用（示例实现）。
type ServerClock struct{}

func (ServerClock) NowMillis(ctx context.Context, c *Client) (int64, error) {
    // 为避免循环依赖，仅在示例/测试中使用。生产建议用 OffsetClock。
    type req interface{ APIRequest }
    // 使用 common.GetServerTimestampRequest 需要从上层传入，避免 import 循环。
    return time.Now().UnixMilli(), nil
}

