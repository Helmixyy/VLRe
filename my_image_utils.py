import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def imRectBox(img, rect, color, alpha=0.2, addText=None, line_thickness=2, fontC=(0, 0, 0)):
    """
    使用PIL绘制矩形框，支持添加文本和半透明填充
    :param img: 输入图像（numpy数组）
    :param rect: 矩形坐标 [x1, y1, x2, y2]
    :param color: 颜色 (R, G, B)
    :param alpha: 透明度，0为完全透明，1为不透明
    :param addText: 矩形框上方显示的文本
    :param line_thickness: 线条粗细
    :param fontC: 字体颜色
    :return: 添加了矩形框的图像
    """
    img = img.copy()
    # 转换为PIL图像
    if isinstance(img, np.ndarray):
        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    else:
        img_pil = img
    
    # 创建绘图对象
    draw = ImageDraw.Draw(img_pil, 'RGBA')
    
    # 获取矩形坐标
    x1, y1, x2, y2 = rect
    
    # 确保颜色是元组而不是列表
    if isinstance(color, list):
        color = tuple(color)
    
    # 确保填充颜色是有效的
    try:
        # 绘制半透明填充
        if alpha > 0:
            fill_color = (*color, int(255 * alpha))
            draw.rectangle([x1, y1, x2, y2], fill=fill_color)
    except Exception as e:
        print(f"填充矩形错误: {e}, color={color}")
    
    # 绘制矩形边框
    try:
        for i in range(line_thickness):
            draw.rectangle([x1 + i, y1 + i, x2 - i, y2 - i], outline=color)
    except Exception as e:
        print(f"绘制边框错误: {e}, color={color}")
        # 如果颜色格式有问题，使用默认颜色
        for i in range(line_thickness):
            draw.rectangle([x1 + i, y1 + i, x2 - i, y2 - i], outline=(255, 0, 0))
    
    # 添加文本
    if addText:
        try:
            # 尝试加载一个通用字体
            font = ImageFont.truetype("arial.ttf", 20)
        except IOError:
            # 如果加载失败，使用默认字体
            font = ImageFont.load_default()
        
        # 使用textbbox替代已弃用的textsize方法
        text_bbox = draw.textbbox((0, 0), addText, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # 计算文本位置
        text_x = max(0, x1)
        text_y = max(0, y1 - text_height - 2)
        
        # 确保文本背景颜色是元组
        bg_color = color if isinstance(color, tuple) else (255, 0, 0)
        if isinstance(fontC, list):
            fontC = tuple(fontC)
        
        # 绘制文本背景
        try:
            draw.rectangle([text_x, text_y, text_x + text_width, text_y + text_height], 
                          fill=bg_color)
        except Exception as e:
            print(f"绘制文本背景错误: {e}, bg_color={bg_color}")
            # 如果颜色格式有问题，使用默认颜色
            draw.rectangle([text_x, text_y, text_x + text_width, text_y + text_height], 
                          fill=(255, 0, 0))
        
        # 绘制文本
        try:
            draw.text((text_x, text_y), addText, fill=fontC, font=font)
        except Exception as e:
            print(f"绘制文本错误: {e}, fontC={fontC}")
            # 如果颜色格式有问题，使用默认颜色
            draw.text((text_x, text_y), addText, fill=(0, 0, 0), font=font)
    
    # 转回numpy数组
    if isinstance(img, np.ndarray):
        img_result = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        return img_result
    else:
        return img_pil

def imRectEdge(img, rect, color, alpha=0.2, addText=None, line_thickness=2, fontC=(0, 0, 0)):
    """
    使用PIL绘制边缘的矩形框，支持添加文本和半透明填充
    :param img: 输入图像（numpy数组）
    :param rect: 矩形坐标 [x1, y1, x2, y2]
    :param color: 颜色 (R, G, B)
    :param alpha: 透明度，0为完全透明，1为不透明
    :param addText: 矩形框上方显示的文本
    :param line_thickness: 线条粗细
    :param fontC: 字体颜色
    :return: 添加了矩形框的图像
    """
    img = img.copy()
    # 转换为PIL图像
    if isinstance(img, np.ndarray):
        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    else:
        img_pil = img
    
    # 创建绘图对象
    draw = ImageDraw.Draw(img_pil, 'RGBA')
    
    # 获取矩形坐标
    x1, y1, x2, y2 = rect
    
    # 确保颜色是元组而不是列表
    if isinstance(color, list):
        color = tuple(color)
    
    # 绘制边缘
    try:
        width = x2 - x1
        height = y2 - y1
        
        # 绘制矩形边框的四个顶点
        edge_length = min(width, height) // 3  # 边缘长度为矩形的1/3
        
        # 左上角
        draw.line([(x1, y1), (x1 + edge_length, y1)], fill=color, width=line_thickness)
        draw.line([(x1, y1), (x1, y1 + edge_length)], fill=color, width=line_thickness)
        
        # 右上角
        draw.line([(x2, y1), (x2 - edge_length, y1)], fill=color, width=line_thickness)
        draw.line([(x2, y1), (x2, y1 + edge_length)], fill=color, width=line_thickness)
        
        # 左下角
        draw.line([(x1, y2), (x1 + edge_length, y2)], fill=color, width=line_thickness)
        draw.line([(x1, y2), (x1, y2 - edge_length)], fill=color, width=line_thickness)
        
        # 右下角
        draw.line([(x2, y2), (x2 - edge_length, y2)], fill=color, width=line_thickness)
        draw.line([(x2, y2), (x2, y2 - edge_length)], fill=color, width=line_thickness)
    except Exception as e:
        print(f"绘制边缘错误: {e}, color={color}")
        # 如果颜色格式有问题，使用默认颜色
        # 这里略去重复绘制代码
    
    # 添加文本
    if addText:
        try:
            # 尝试加载一个通用字体
            font = ImageFont.truetype("arial.ttf", 20)
        except IOError:
            # 如果加载失败，使用默认字体
            font = ImageFont.load_default()
        
        # 使用textbbox替代已弃用的textsize方法
        text_bbox = draw.textbbox((0, 0), addText, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # 计算文本位置
        text_x = max(0, x1)
        text_y = max(0, y1 - text_height - 2)
        
        # 确保文本背景颜色是元组
        bg_color = color if isinstance(color, tuple) else (255, 0, 0)
        if isinstance(fontC, list):
            fontC = tuple(fontC)
        
        # 绘制文本背景
        try:
            draw.rectangle([text_x, text_y, text_x + text_width, text_y + text_height], 
                          fill=bg_color)
        except Exception as e:
            print(f"绘制文本背景错误: {e}, bg_color={bg_color}")
            # 如果颜色格式有问题，使用默认颜色
            draw.rectangle([text_x, text_y, text_x + text_width, text_y + text_height], 
                          fill=(255, 0, 0))
        
        # 绘制文本
        try:
            draw.text((text_x, text_y), addText, fill=fontC, font=font)
        except Exception as e:
            print(f"绘制文本错误: {e}, fontC={fontC}")
            # 如果颜色格式有问题，使用默认颜色
            draw.text((text_x, text_y), addText, fill=(0, 0, 0), font=font)
    
    # 转回numpy数组
    if isinstance(img, np.ndarray):
        img_result = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        return img_result
    else:
        return img_pil

def drawRectBox(img, rect, color=(255, 0, 0), alpha=0.2, addText=None, fontC=(0, 0, 0), line_thickness=2):
    """
    绘制矩形框的封装函数
    :param img: 输入图像
    :param rect: 矩形坐标 [x1, y1, x2, y2]
    :param color: 颜色 (R, G, B)
    :param alpha: 透明度
    :param addText: 文本
    :param fontC: 字体颜色
    :param line_thickness: 线条粗细
    :return: 处理后的图像
    """
    # 如果输入为空，直接返回原图像
    if img is None or rect is None:
        return img
    
    # 确保颜色是元组而不是列表
    try:
        if isinstance(color, list):
            color = tuple(color)
        # 检查颜色元组的长度是否为3，如果不是，使用默认颜色
        if not isinstance(color, tuple) or len(color) != 3:
            color = (255, 0, 0)  # 默认使用红色
    except:
        color = (255, 0, 0)  # 出现异常时使用红色
        
    # 处理字体颜色
    try:
        if isinstance(fontC, list):
            fontC = tuple(fontC)
        if not isinstance(fontC, tuple) or len(fontC) != 3:
            fontC = (0, 0, 0)  # 默认使用黑色
    except:
        fontC = (0, 0, 0)  # 出现异常时使用黑色
    
    # 处理矩形坐标
    try:
        rect = [int(v) for v in rect]  # 确保矩形坐标是整数
    except:
        return img  # 坐标无效时返回原图像
    
    return imRectBox(img, rect, color, alpha, addText, line_thickness, fontC)

def drawRectEdge(img, rect, color=(255, 0, 0), alpha=0.2, addText=None, fontC=(0, 0, 0), line_thickness=2):
    """
    绘制矩形边缘框的封装函数
    :param img: 输入图像
    :param rect: 矩形坐标 [x1, y1, x2, y2]
    :param color: 颜色 (R, G, B)
    :param alpha: 透明度
    :param addText: 文本
    :param fontC: 字体颜色
    :param line_thickness: 线条粗细
    :return: 处理后的图像
    """
    # 如果输入为空，直接返回原图像
    if img is None or rect is None:
        return img
    
    # 确保颜色是元组而不是列表
    try:
        if isinstance(color, list):
            color = tuple(color)
        # 检查颜色元组的长度是否为3，如果不是，使用默认颜色
        if not isinstance(color, tuple) or len(color) != 3:
            color = (255, 0, 0)  # 默认使用红色
    except:
        color = (255, 0, 0)  # 出现异常时使用红色
        
    # 处理字体颜色
    try:
        if isinstance(fontC, list):
            fontC = tuple(fontC)
        if not isinstance(fontC, tuple) or len(fontC) != 3:
            fontC = (0, 0, 0)  # 默认使用黑色
    except:
        fontC = (0, 0, 0)  # 出现异常时使用黑色
    
    # 处理矩形坐标
    try:
        rect = [int(v) for v in rect]  # 确保矩形坐标是整数
    except:
        return img  # 坐标无效时返回原图像
    
    return imRectEdge(img, rect, color, alpha, addText, line_thickness, fontC) 