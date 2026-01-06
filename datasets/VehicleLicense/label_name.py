# -*- coding: utf-8 -*-
"""
车牌识别系统
运行本项目需要python3.8及以下依赖库（完整库见requirements.txt）：
    opencv-python==4.5.5.64
    tensorflow==2.9.1
    PyQt5==5.15.6
    scikit-image==0.19.3
    torch==1.8.0
    keras==2.9.0
    Pillow==9.0.1
    scipy==1.8.0
点击运行主程序runMain.py，程序所在文件夹路径中请勿出现中文
"""
Chinese_name = {
    "License_Plate": "车牌",
    "cars": "汽车",
    "motorcyle": "摩托车",
    "truck": "卡车"
}
Label_list = list(Chinese_name.values())
