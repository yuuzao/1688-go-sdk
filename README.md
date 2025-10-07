# 1688 Go SDK

一个面向 1688 OpenAPI 的 Go SDK（Go 1.25），参考了 Python 版 SDK 的签名、系统参数与 URL 规则，并提供了可复用的日志/鉴权/时间戳策略与文件上传能力。项目内置 Python → Go 的生成工具，便于从官方/既有 Python 定义同步 API。

**NOTE: 暂时只包含订单管理解决方案（加密服务商新版）**

核心目标：
- 与 Python 版一致的签名、参数与路径规则。
- 易扩展：新增 API 只需新增一个 Request/Response 文件，无需修改核心。
- 结构化日志、可插拔时间戳与 Token 提供者，便于排错与生产化使用。

## 安装

```bash
go get github.com/yuuzao/1688-go-sdk
```

## 快速开始

```go
package main

import (
    "context"
    "fmt"
    "github.com/yuuzao/1688-go-sdk/sdk"
    "github.com/yuuzao/1688-go-sdk/api/common"
)

func main() {
    cli := sdk.NewClient(
        sdk.WithServer("gw.open.1688.com"),
        sdk.WithAppInfo("1000000", "aaaaaaaaaaaa"),
        sdk.WithTimestampSource(sdk.LocalClock()),
    )

    // 获取服务器时间戳（毫秒）
    var ts int64
    if err := cli.Do(context.Background(), common.NewGetServerTimestamp(), &ts); err != nil {
        panic(err)
    }
    fmt.Println(ts)
}
```

## 项目结构
- `sdk/` 核心库：`client.go`, `request.go`, `sign.go`, `transport.go`, `errors.go`, `file.go`, `timestamp.go`, `options.go`, `logger.go` 等。
- `api/common/` 常用系统 API 示例：`get_server_timestamp.go`, `auth_*`。
- `api/biz/` 业务 API 注册：
  - `registry_static.go` 内置所有已支持 API 的静态注册表（按命名空间分组注释）。
  - `registry.go` 注册中心（`Register/New/NewByURI`）。
  - `registry_load.go` 开发辅助（可从 Python 源动态解析，不影响发版）。
- `tools/` Python 源与生成器：
  - `tools/aop/` Python 版 SDK（仅作为生成输入，不参与 Go 构建）。
  - `tools/generate.py` 生成 `api/biz/registry_static.go`。
- `Makefile` 快捷命令：`make generate`、`make test`、`make fmt`。

## 从 Python 更新 API 注册表
当 `tools/aop/api/biz` 中的 Python 定义变化时，可一键同步：

```bash
make generate   # 调用 tools/generate.py 生成 api/biz/registry_static.go
make test       # 运行所有单测
```

或手动执行：

```bash
INPUT_DIR=tools/aop/api/biz OUTPUT=api/biz/registry_static.go \
python3 tools/generate.py
```

生成器会按命名空间分组（如 logistics、trade、product 等）写入注释，便于查阅。

## 日志与排障
- 默认仅在错误时记录响应体的前 2KB 预览，并自动脱敏 `access_token` 与 `secret`。
- 可通过 `WithLogger`、`WithLogLevel`、`WithLogBody` 等选项进行控制。

示例（接入 slog）：

```go
import (
  "log/slog"
  "github.com/yuuzao/1688-go-sdk/sdk"
)

cli := sdk.NewClient(
  sdk.WithServer("gw.open.1688.com"),
  sdk.WithAppInfo("APPKEY","SECRET"),
  sdk.WithSlog(slog.Default()),
)
```

## 扩展新 API
在 `api/<group>/` 新增 `FooRequest` 与 `FooResponse`，其中请求结构体嵌入 `BaseRequest`，按照 API 文档覆盖必要钩子（是否签名、是否需要 token 等）与必填参数列表即可。

也可以使用通用封装与注册表（已内置静态注册表，覆盖本仓库 Python SDK 中的全部 biz API）：

```go
import (
  "context"
  "github.com/yuuzao/1688-go-sdk/sdk"
  "github.com/yuuzao/1688-go-sdk/api/biz"
)

func callProductGet(cli *sdk.Client) error {
  // 使用静态注册表，直接按名称构造请求：
  req := biz.New("AlibabaProductGet")
  req.ParamsMap["productID"] = 123
  req.ParamsMap["webSite"] = "1688"
  req.ParamsMap["scene"] = "normal"
  var resp map[string]any
  return cli.Do(context.Background(), req, &resp)
}
```

完全通用（不依赖注册表）：

```go
req := &sdk.GenericRequest{
  APIURI:    "1/com.alibaba.product/alibaba.product.get",
  Sign:      true,
  Auth:      true,
  HTTPS:     false,
  Required:  []string{"productID","webSite","scene"},
  ParamsMap: map[string]any{"productID":123,"webSite":"1688","scene":"normal"},
}
var out map[string]any
if err := cli.Do(ctx, req, &out); err != nil { /* handle */ }
```

## 文件上传示例（multipart）

当某些参数为 `byte[]` 时，使用 `sdk.FileItem`：

```go
req := &sdk.GenericRequest{
  APIURI:    "1/com.alibaba.xxx/upload",
  Sign:      true, Auth: true,
  Multipart: []string{"image"},
  ParamsMap: map[string]any{
    "image": sdk.FileItem{Name:"a.png", Content: bytes.NewReader(imgBytes)},
    "name":  "hello",
  },
}
var resp map[string]any
_ = cli.Do(ctx, req, &resp)
```

## 错误处理
- `ApiError`：远端返回的业务错误，包含 `error_code/error_message/exception/request_id`。
- `AopError`：本地异常（参数缺失/签名配置错误/网络超时/JSON 解析失败等）。

## 测试

```bash
make test
```

## 兼容性
- Go 1.25+（go.mod: `go 1.25`）。
- 模块名：`github.com/yuuzao/1688-go-sdk`（发布时按你的仓库地址更新）。

## 贡献
- 对常用 API，欢迎补充强类型 `Request/Response` 到 `api/<group>/`，其余使用注册表 + `GenericRequest` 兜底。
- 如需在 CI 中校验生成产物一致性，可在工作流里执行 `make generate && git diff --exit-code`。
