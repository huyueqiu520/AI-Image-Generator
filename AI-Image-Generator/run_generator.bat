@echo off
echo AI图片生成工具
echo.

REM 检查是否安装了Python
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python。请先安装Python。
    pause
    exit /b 1
)

echo 发现Python环境: 
python --version
echo.

REM 检查并安装依赖（如果需要）
echo 检查依赖包...
pip show openai >nul 2>&1
if errorlevel 1 (
    echo 正在安装依赖包...
    pip install openai==0.28.1
    pip install Pillow==10.0.1
    pip install requests==2.31.0
    echo 依赖包安装完成。
) else (
    echo 依赖包已安装。
)
echo.

REM 运行AI图片生成器
echo 启动AI图片生成工具...
echo 工具将自动获取API密钥（如果已配置）
echo.
cd /d C:\Users\Administrator\Desktop\AI-Image-Generator
python ai_image_generator.py

pause