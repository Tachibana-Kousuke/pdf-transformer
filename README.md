# PDF Transformer

PDF Transformer 是一款用于批量处理 PDF 文件的工具，支持将 PDF 文件转换为 Word、Markdown、TXT 格式，同时支持多个 PDF 合并为一个文件。

## 功能特点

- **PDF 转 Word**：将 PDF 文件转换为可编辑的 Word 文档。
- **PDF 转 Markdown**：将 PDF 文件转换为 Markdown 格式，保留文本和部分格式。
- **PDF 转 TXT**：将 PDF 文件中的文本提取到 TXT 文件中，支持批量转换。
- **合并多个 PDF**：将多个 PDF 文件合并成一个 PDF 文件。

## 使用说明

### 安装依赖

确保你已经安装了 Python 3.x，并且已经安装了必要的依赖,如果没有，你可以使用一以下命令安装：

```bash
pip install PyMuPDF pdf2docx markdownify pdfminer.six
```

### 使用方式

1. 运行 `pdftransformer.py`，打开 GUI 界面。
2. 选择对应的功能（PDF 转 Word、PDF 转 Markdown、PDF 转 TXT、合并 PDF）。
3. 根据提示选择文件，并选择目标保存路径。
4. 执行操作后，文件会被自动处理并保存。

### 功能详解

#### PDF 转 Word

该功能允许你将 PDF 文件转换为 Word 格式，所有文本内容将保留，并转换成可编辑的格式。

#### PDF 转 Markdown

将 PDF 文件中的文本内容转换为 Markdown 格式，支持标题、段落、列表等基本格式。此功能特别适用于将 PDF 内容迁移到博客或其他基于 Markdown 的平台。

#### PDF 转 TXT

该功能将 PDF 文件中的文本提取出来，并保存为 TXT 文件。适用于需要快速获取 PDF 中的纯文本信息的场景。

#### 合并多个 PDF

此功能允许用户选择多个 PDF 文件，并将它们合并成一个新的 PDF 文件。适合需要将多个 PDF 文件合并成一个文档的情况。

## 已知问题

目前，本工具存在一个已知的缺陷：

- **数学公式的转换**：在转换 PDF 为 TXT 或 Markdown 格式时，数学公式无法完美转换。公式会以乱码输出。

我们正在继续改进这个功能，未来版本中将会改善数学公式的转换效果。

## 打包成 EXE

本工具已打包为 Windows 可执行文件（EXE）。如果你不希望在使用时看到命令行窗口，可以使用以下命令进行打包：

```bash
pyinstaller --onefile --noconsole pdftransformer.py
```

### 注意：

- 你可以直接运行生成的 EXE 文件，无需安装 Python 环境。
- 目前该工具仅支持 Windows 操作系统。

## 开发者

本工具由 [Tachibana Kousuke](https://github.com/Tachibana-Kousuke) 开发。如果你有任何问题或建议，欢迎提交 issue 或 pull request。

## 许可证

MIT License