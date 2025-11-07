AI图片生成工具使用说明
===================

1. 环境要求
   - Python 3.7+ (当前系统已安装Python 3.12.10)
   - 已安装所需依赖包

2. 依赖安装
   所有依赖包已安装，包含：
   - openai==0.28.1
   - Pillow==10.0.1
   - requests==2.31.0

3. API密钥设置（支持多种方式）
   需要OpenAI API密钥才能使用此工具。
   
   自动获取方式（按优先级排序）：
   a) 环境变量: set OPENAI_API_KEY=your_api_key_here
   b) 配置文件: config.json（同目录下）
   c) 用户目录: ~/.openai_config.json
   d) 运行时手动输入并可选择保存到配置文件

4. 运行程序
   python ai_image_generator.py

5. 功能
   - 根据文本描述生成图片
   - 生成图片变体(需要提供原始图片)

6. 图片尺寸选项
   - 256x256
   - 512x512
   - 1024x1024

7. 快速开始
   - 第一次运行: 直接运行程序，按提示输入API密钥并选择保存
   - 之后运行: 直接运行程序即可自动获取API密钥
   - 运行命令: cd C:\Users\Administrator\Desktop\AI图片制作 && python ai_image_generator.py