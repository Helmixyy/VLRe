# 基于YOLOv8v5/LPRNet的车牌检测系统

本系统是一个基于深度学习的车牌检测与识别系统，使用YOLOv8/v5进行车牌定位，LPRNet进行车牌字符识别，同时结合颜色识别模型对车牌颜色进行分类。系统提供了友好的图形用户界面，支持图片、视频和摄像头实时检测功能。

## 环境要求

- Python 3.10
- PySide6 (Qt for Python)
- PyTorch
- OpenCV
- 其他依赖见requirements.txt

## 安装配置

1. 使用Anaconda创建Python环境：
   ```
   conda create -n env_rec python=3.10
   conda activate env_rec
   ```

2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 系统架构

### 核心文件

- **YOLOv8v5PlateModel.py**: 车牌检测模型类，集成了YOLO车牌定位和LPRNet字符识别功能
- **LPRNet.py**: 车牌字符识别网络实现，包含中国车牌字符集定义
- **PlateColorModel.py**: 车牌颜色识别模型，基于HSV颜色空间分析

### 界面文件

- **Recognition_UI.py**: 主界面UI定义文件，由UI设计工具生成
- **System_noLogin.py**: 无登录版本的系统主界面实现
- **System_login.py**: 带登录验证的系统主界面实现
- **LoginWindow.py**: 登录窗口实现
- **LoginForm.py**: 登录窗口UI定义文件

### 启动文件

- **run_main_noLogin.py**: 启动无登录界面版本的主程序
- **run_main_login.py**: 启动带登录验证的主程序
- **run_test_image.py**: 图片测试程序
- **run_test_video.py**: 视频测试程序
- **run_test_camera.py**: 摄像头测试程序
- **run_train_model.py**: 模型训练程序

### 数据文件

- **datasets/VehicleLicense/**: 车牌数据集目录
  - **label_name.py**: 标签名称定义
  - **__init__.py**: 数据集初始化文件
  - **train/**: 训练数据
  - **valid/**: 验证数据
  - **test/**: 测试数据
  - **VehicleLicense.yaml**: 数据集配置文件

### 配置文件

- **themes/Settings_main.yaml**: 主界面样式和元素配置
- **themes/main_dark_back.qss**: 主界面QSS样式表

### 其他文件

- **weights/**: 模型权重存储目录
- **icons/**: 系统UI图标资源
- **UserDatabase.db**: 用户数据库
- **requirements.txt**: 依赖库列表

## 系统功能

1. **车牌检测与识别**：
   - 支持中国各类车牌的检测与字符识别
   - 支持车牌颜色识别

2. **多种输入方式**：
   - 支持图片文件输入
   - 支持视频文件输入
   - 支持摄像头实时输入

3. **结果展示**：
   - 实时显示检测结果与置信度
   - 支持结果表格展示
   - 支持结果保存为图片、视频和CSV文件

4. **系统配置**：
   - 可调节检测阈值
   - 可选择不同模型
   - 支持用户登录管理（登录版本）

## 使用方法

1. 启动系统：
   ```
   # 无登录版本
   python run_main_noLogin.py
   
   # 带登录版本
   python run_main_login.py
   ```

2. 选择输入源：
   - 点击图片按钮选择图片文件
   - 点击视频按钮选择视频文件
   - 点击摄像头按钮启动摄像头实时检测

3. 调整参数：
   - 使用界面上的滑块调整检测置信度阈值
   - 使用界面上的滑块调整IOU阈值

4. 查看和保存结果：
   - 检测结果将在主界面显示
   - 点击保存按钮可将结果保存为文件

## 注意事项
- 初次运行时请确保已下载模型权重文件并放置于weights目录

- 使用GPU加速时，请确保已安装对应版本的CUDA和cuDNN 
