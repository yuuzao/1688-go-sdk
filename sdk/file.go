package sdk

import "io"

// FileItem 表示要上传的文件，与 Python SDK 的 FileItem 对齐。
// Name 为服务器侧看到的文件名；Content 为文件流（可为内存/文件/网络流）。
type FileItem struct {
    Name    string
    Content io.Reader
}

