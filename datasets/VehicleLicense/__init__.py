# -*- coding: utf-8 -*-

__version__ = '2.0'
__author__ = '系统开发者'
__email__ = ''
__url__ = ''

SYSTEM_INFO = ("基于YOLOv8/v5的车牌检测系统v1.0\n"
               "用于车牌检测、识别和分析\n\n"
               "本系统仅供学习和研究使用")

ENV_CONFIG = ("[配置环境]\n"
              "请按照给定的python版本配置环境，否则可能会因依赖不兼容而出错\n"
              "(1)使用anaconda新建python3.10环境:\n"
              "conda create -n env_rec python=3.10\n"
              "(2)激活创建的环境:\n"
              "conda activate env_rec\n"
              "(3)使用pip安装所需的依赖，可通过requirements.txt:\n"
              "pip install -r requirements.txt\n")

with open('./环境配置.txt', 'w', encoding='utf-8') as f:
    f.writelines(ENV_CONFIG + "\n\n" + SYSTEM_INFO)
