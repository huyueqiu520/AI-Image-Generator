# AI图片生成工具

一个基于AI的图片生成工具，支持多种API提供商，可根据文本描述生成图片。

## 功能特性

- 根据文本描述生成图片
- 支持多种图片尺寸（256x256, 512x512, 1024x1024）
- 支持图片变体生成
- 支持多种API提供商（OpenAI、百度AI、阿里云等）
- 自动API密钥管理

## 环境要求

- Python 3.7+
- 有效的API密钥

## 安装步骤

1. 克隆项目：
   ```bash
   git clone <repository-url>
   cd AI图片生成工具
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## API配置

在使用本工具前，请配置API密钥：

### 方法1：环境变量
```bash
export API_KEY=your_api_key_here      # Linux/Mac
set API_KEY=your_api_key_here         # Windows
```

### 方法2：配置文件
编辑 `config.json` 文件：
```json
{
  "api_key": "your_api_key_here",
  "provider": "openai"
}
```

### 方法3：首次运行时输入
程序将提示您输入API密钥，并可选择保存。

## 使用方法

1. 配置API密钥（见上文）
2. 运行程序：
   ```bash
   python ai_image_generator.py
   ```
3. 按照提示输入图片描述和参数

## 支持的API提供商

- OpenAI（默认）
- 百度AI
- 阿里云
- 腾讯云

## 项目结构

```
AI图片生成工具/
├── ai_image_generator.py    # 主程序文件
├── config.json             # API配置文件
├── requirements.txt        # 依赖列表
├── run_generator.bat       # Windows启动脚本
├── API_CONFIG_NOTICE.txt   # API配置说明
├── USAGE_GUIDE.md          # 详细使用说明
├── DISCLAIMER.md           # 免责声明
└── README.md              # 项目说明
```

## 安全提醒

- 请妥善保管您的API密钥
- 不要在公开代码中暴露密钥
- 定期检查API使用情况和账单

## 免责声明

使用本工具前请仔细阅读 [免责声明](DISCLAIMER.md)。

## 贡献

欢迎提交Issue和Pull Request来改进本项目。

## 许可证

[在此处添加您的许可证信息]