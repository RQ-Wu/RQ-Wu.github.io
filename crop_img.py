from PIL import Image
import os

def center_crop_square(image_path, size):
    """
    中心裁剪图片为 size x size 的正方形，并保存覆盖原文件。
    
    Args:
        image_path (str): 要处理的图片路径
        size (int): 裁剪后正方形的边长（单位：像素）
    """
    # 打开图片
    img = Image.open(image_path)
    width, height = img.size

    # 计算中心点
    center_x, center_y = width // 2, height // 2

    # 计算左上和右下坐标
    left = max(center_x - size // 2, 0)
    upper = max(center_y - size // 2, 0)
    right = min(left + size, width)
    lower = min(upper + size, height)

    # 裁剪
    img_cropped = img.crop((left, upper, right, lower))

    # 如果原图太小，resize 到目标 size（可选）
    if img_cropped.size != (size, size):
        img_cropped = img_cropped.resize((size, size), Image.LANCZOS)

    # 保存覆盖原图
    img_cropped.save(image_path)

def keep_left_half(image_path):
    """
    只保留图像的左半部分，覆盖原图保存。

    Args:
        image_path (str): 图像路径
    """
    img = Image.open(image_path)
    width, height = img.size

    # 仅保留左半区域 (从左边0到width的一半)
    left_half = img.crop((0, 0, width // 2, height))

    # 覆盖原图保存
    left_half.save(image_path)

center_crop_square('/home/users/ruiqi.wu/RQ-Wu.github.io/projects/DIPO/pm_result/5/gt_1.png', 330)