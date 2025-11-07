AI图片生成工具使用说明
====================

## 目录
1. [简介](#简介)
2. [系统要求](#系统要求)
3. [安装步骤](#安装步骤)
4. [API配置](#api配置)
5. [使用方法](#使用方法)
6. [功能详解](#功能详解)
7. [API提供商设置](#api提供商设置)
8. [故障排除](#故障排除)
9. [注意事项](#注意事项)

## 简介
AI图片生成工具是一个基于人工智能的图片生成应用程序，可以根据文本描述生成高质量的图片。该工具支持多种API提供商，包括OpenAI、百度AI、阿里云和腾讯云。

## 系统要求
- 操作系统：Windows 7及以上版本，macOS 10.12及以上版本，或Linux发行版
- Python版本：Python 3.7及以上版本
- 网络连接：用于API调用
- 硬盘空间：至少50MB可用空间

## 安装步骤

### 方法一：从GitHub克隆
1. 打开命令行终端
2. 执行命令：
   ```
   git clone <repository-url>
   cd AI图片生成工具
   ```
3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

### 方法二：下载ZIP文件
1. 从GitHub下载项目ZIP文件
2. 解压缩到任意目录
3. 安装依赖：
   ```
   cd AI图片生成工具
   pip install -r requirements.txt
   ```

## API配置

### 配置文件方式（推荐）
1. 打开 `config.json` 文件
2. 填入您的API密钥和提供商：
   ```json
   {
     "api_key": "your_api_key_here",
     "provider": "openai"
   }
   ```
3. 保存文件

### 环境变量方式
- Windows：
  ```
  set API_KEY=your_api_key_here
  set PROVIDER=openai
  ```
- Linux/macOS：
  ```
  export API_KEY=your_api_key_here
  export PROVIDER=openai
  ```

### 首次运行时配置
运行程序后，系统会提示您选择API提供商并输入API密钥。

## 使用方法

### 命令行运行
```
python ai_image_generator.py
```

### 使用批处理文件（仅Windows）
```
run_generator.bat
```

## 功能详解

### 图片生成
1. 启动程序后，按提示输入图片描述
2. 选择图片尺寸（256x256, 512x512, 1024x1024）
3. 指定输出文件名
4. 程序将生成图片并保存到指定位置

### 图片变体生成
（仅支持OpenAI）通过现有图片生成变体：
1. 使用代码中的 `generate_image_variation` 方法
2. 提供原始图片路径
3. 程序将生成原始图片的变体

## API提供商设置

### OpenAI
1. 访问 https://platform.openai.com/api-keys
2. 创建新的API密钥
3. 配置提供商为 `openai`

### 百度AI
1. 访问 https://console.bce.baidu.com/ai/
2. 在文心一言大模型中获取API密钥
3. 配置提供商为 `baidu`

### 阿里云
1. 访问 https://www.aliyun.com/
2. 在通义万相服务中获取API密钥
3. 配置提供商为 `aliyun`

### 腾讯云
1. 访问 https://cloud.tencent.com/
2. 在AI绘画服务中获取API密钥
3. 配置提供商为 `tencent`

## 故障排除

### 常见问题

#### 1. "请提供API密钥"错误
- 检查API密钥是否正确输入
- 确认环境变量或配置文件设置正确

#### 2. 网络连接错误
- 检查网络连接是否正常
- 如果在受限网络环境中，可能需要配置代理

#### 3. 图片生成失败
- 检查API配额是否已用完
- 确认API密钥有相应的调用权限

#### 4. 模块导入错误
- 重新安装依赖：`pip install -r requirements.txt`
- 检查Python版本是否符合要求

## 注意事项

### 安全提醒
- 请妥善保管您的API密钥
- 不要在GitHub等公共平台上暴露API密钥
- 定期轮换API密钥
- 注意API调用费用，避免超出预算

### 使用限制
- 遵守各API提供商的使用条款
- 避免生成受版权保护或违法内容
- 注意API调用频率限制

### 文件管理
- 生成的图片将保存在程序运行目录下
- 请确保有足够的存储空间
- 定期清理不需要的图片文件

## 更新日志
- v1.0.0：初始版本，支持OpenAI DALL-E
- v1.1.0：添加多API提供商支持
- v1.2.0：增加自动配置功能

## 贡献
欢迎提交Issue和Pull Request来改进本项目。

## 许可证
本项目采用MIT许可证，详见LICENSE文件。