import os
import argparse
import torch
import yaml
from ultralytics import YOLO
from QtFusion.path import abs_path

device = "0" if torch.cuda.is_available() else "cpu"

def train_model(model_version='v8'):
    workers = 1
    batch = 8

    data_name = "VehicleLicense"
    data_path = abs_path(f'datasets/{data_name}/{data_name}.yaml', path_type='current')
    unix_style_path = data_path.replace(os.sep, '/')

    # 获取目录路径
    directory_path = os.path.dirname(unix_style_path)
    # 读取YAML文件，保持原有顺序
    with open(data_path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    # 修改path项
    if 'path' in data:
        data['path'] = directory_path
        # 将修改后的数据写回YAML文件
        with open(data_path, 'w') as file:
            yaml.safe_dump(data, file, sort_keys=False)

    if model_version == 'v5':
        # 使用YOLOv8模型
        print("正在使用YOLOv8模型进行训练...")
        model = YOLO(abs_path('./weights/yolov8n.pt', path_type='current'), task='detect')
        model_name = 'train_v8_' + data_name
    else:
        # 使用YOLOv5模型
        print("正在使用YOLOv5模型进行训练...")
        model = YOLO(abs_path('./weights/yolov5nu.pt', path_type='current'), task='detect')
        model_name = 'train_v5_' + data_name

    # 开始训练模型
    results = model.train(
        data=data_path,  # 指定训练数据的配置文件路径
        device=device,   # 自动选择设备进行训练
        workers=workers, # 指定工作进程数量
        imgsz=640,       # 指定输入图像的大小为640x640
        epochs=120,      # 指定训练120个epoch
        batch=batch,     # 指定每个批次的大小
        name=model_name  # 指定训练任务的名称
    )
    
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='训练车牌识别模型')
    parser.add_argument('--model', type=str, default='v8', choices=['v5', 'v8'],
                      help='选择训练模型版本: v5 或 v8 (默认: v8)')
    args = parser.parse_args()
    
    train_model(model_version=args.model)
