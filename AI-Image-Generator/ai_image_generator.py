import os
import openai
from PIL import Image
import requests
from io import BytesIO
import json
import sys

class AIImageGenerator:
    def __init__(self, api_key=None, provider=None):
        """
        初始化AI图片生成器
        :param api_key: API密钥，如果不提供，则尝试从配置文件或其他来源获取
        :param provider: API提供商 ('openai', 'baidu', 'aliyun', 'tencent')
        """
        # 获取配置
        config = self._get_config()
        self.api_key = api_key or config.get('api_key') or self._get_api_key()
        self.provider = provider or config.get('provider', 'openai')
        
        if not self.api_key:
            raise ValueError("请提供API密钥，或设置环境变量，或在config.json中配置API密钥")

    def _get_config(self):
        """
        从配置文件获取配置信息
        """
        config_paths = [
            os.path.join(os.path.dirname(__file__), 'config.json'),
            os.path.join(os.path.expanduser('~'), '.ai_config.json'),
            os.path.join(os.path.expanduser('~'), 'Documents', '.ai_config.json')
        ]
        
        for config_path in config_paths:
            if os.path.exists(config_path):
                try:
                    with open(config_path, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except Exception:
                    continue
        return {}

    def _get_api_key(self):
        """
        自动获取API密钥的方法
        """
        # 首先尝试从环境变量获取
        api_key = os.getenv('API_KEY') or os.getenv('OPENAI_API_KEY')
        if api_key:
            return api_key
            
        # 然后尝试从配置文件获取
        config = self._get_config()
        api_key = config.get('api_key')
        if api_key:
            return api_key
            
        # 如果都没有找到，提示用户输入
        return self._prompt_for_api_key()

    def _prompt_for_api_key(self):
        """
        提示用户输入API密钥并保存到配置文件
        """
        print("未找到API密钥，请选择API提供商并输入相应的API密钥：")
        print("1. OpenAI")
        print("2. 百度AI")
        print("3. 阿里云")
        print("4. 腾讯云")
        
        provider_choice = input("请选择提供商 (1-4): ").strip()
        provider_map = {'1': 'openai', '2': 'baidu', '3': 'aliyun', '4': 'tencent'}
        provider = provider_map.get(provider_choice, 'openai')
        
        api_key = input("请输入API密钥: ").strip()
        
        if api_key:
            # 询问是否保存到配置文件
            save_option = input("是否保存API密钥和提供商到配置文件以便下次自动使用？(y/n): ").strip().lower()
            if save_option == 'y' or save_option == 'yes':
                self._save_config_to_file(api_key, provider)
            return api_key
        else:
            return None

    def _save_config_to_file(self, api_key, provider):
        """
        将API密钥和提供商保存到配置文件
        """
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        try:
            config = {'api_key': api_key, 'provider': provider}
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            print(f"配置已保存到 {config_path}")
        except Exception as e:
            print(f"保存配置时出错: {str(e)}")

    def generate_image(self, prompt, size="1024x1024", output_path="generated_image.png"):
        """
        生成图片
        :param prompt: 图片描述文本
        :param size: 图片大小
        :param output_path: 输出图片路径
        :return: 生成的图片路径
        """
        try:
            if self.provider == 'openai':
                return self._generate_openai_image(prompt, size, output_path)
            elif self.provider == 'baidu':
                return self._generate_baidu_image(prompt, size, output_path)
            elif self.provider == 'aliyun':
                return self._generate_aliyun_image(prompt, size, output_path)
            elif self.provider == 'tencent':
                return self._generate_tencent_image(prompt, size, output_path)
            else:
                print(f"不支持的API提供商: {self.provider}")
                return None
        except Exception as e:
            print(f"生成图片时出错: {str(e)}")
            return None

    def _generate_openai_image(self, prompt, size, output_path):
        """使用OpenAI生成图片"""
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=size
        )
        
        image_url = response['data'][0]['url']
        return self._download_and_save_image(image_url, output_path)

    def _generate_baidu_image(self, prompt, size, output_path):
        """使用百度AI生成图片（占位实现）"""
        print("百度AI图片生成功能尚未实现")
        return None

    def _generate_aliyun_image(self, prompt, size, output_path):
        """使用阿里云生成图片（占位实现）"""
        print("阿里云图片生成功能尚未实现")
        return None

    def _generate_tencent_image(self, prompt, size, output_path):
        """使用腾讯云生成图片（占位实现）"""
        print("腾讯云图片生成功能尚未实现")
        return None

    def _download_and_save_image(self, image_url, output_path):
        """下载并保存图片"""
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        image.save(output_path)
        print(f"图片已保存到: {output_path}")
        return output_path

    def generate_image_variation(self, image_path, size="1024x1024", output_path="variation_image.png"):
        """
        生成图片变体
        :param image_path: 原始图片路径
        :param size: 图片大小
        :param output_path: 输出图片路径
        :return: 生成的图片路径
        """
        try:
            if self.provider == 'openai':
                with open(image_path, "rb") as image_file:
                    response = openai.Image.create_variation(
                        image=image_file,
                        n=1,
                        size=size
                    )
                    
                    image_url = response['data'][0]['url']
                    return self._download_and_save_image(image_url, output_path)
            else:
                print("当前提供商不支持图片变体功能")
                return None
        except Exception as e:
            print(f"生成图片变体时出错: {str(e)}")
            return None

def main():
    # 使用示例
    try:
        # 初始化生成器
        generator = AIImageGenerator()
        
        print(f"当前使用的API提供商: {generator.provider}")
        
        # 生成图片
        prompt = input("请输入图片描述: ")
        size = input("请输入图片尺寸 (256x256, 512x512, 1024x1024，默认为1024x1024): ") or "1024x1024"
        output_path = input("请输入输出文件名 (默认为generated_image.png): ") or "generated_image.png"
        
        print("正在生成图片...")
        result = generator.generate_image(prompt, size, output_path)
        
        if result:
            print("图片生成成功！")
        else:
            print("图片生成失败！")
            
    except ValueError as e:
        print(e)
        print("请先配置API密钥")

if __name__ == "__main__":
    main()