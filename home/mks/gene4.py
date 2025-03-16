import sys
import numpy as np
from PIL import Image, ImageOps
import ctypes
import time

mks_lib = ctypes.CDLL('/home/mks/libColPic.so')

def convert_to_rgb565(image_path, tjc_path, size=200):
    image = Image.open(image_path)
    ratio_image = resize_to_square(image, size)
    ratio_image = ratio_image.convert("RGB")
    # ratio_image.show()
    pixel_values = np.array(ratio_image.getdata(), dtype=np.uint16)
    r = (pixel_values[:, 0] >> 3) & 0x1F
    g = (pixel_values[:, 1] >> 2) & 0x3F
    b = (pixel_values[:, 2] >> 3) & 0x1F

    rgb565_pixel_values = (r << 11) | (g << 5) | b

    rgb16_data = rgb565_pixel_values.flatten().astype(np.uint16).tobytes()
    
    # 调用外部函数处理RGB16数据
    outputdata = bytearray(ratio_image.size[0] * ratio_image.size[1] * 10)
    outputdata_buffer = ctypes.create_string_buffer(len(outputdata))
    outputdata_buffer.raw = outputdata
    outputdata_ptr = ctypes.cast(outputdata_buffer, ctypes.POINTER(ctypes.c_char))
    mks_lib.ColPic_EncodeStr(rgb16_data, ratio_image.size[0], ratio_image.size[1], outputdata_ptr, ratio_image.size[0] * ratio_image.size[1] * 10, 1024)
    
    # 写入输出文件
    # print(outputdata_buffer.raw.decode('utf-8').rstrip('\x00'))
    with open(tjc_path, 'w') as tjc:
      tjc.write(outputdata_buffer.raw.decode('utf-8').rstrip('\x00'))

def resize_to_square(image, size):
    width, height = image.size
    if width > height:
        ratio = size / width
    else:
        ratio = size / height

    if ratio > 1:
        ratio = 1
    
    new_width = int(width * ratio)
    new_height = int(height * ratio)

    resized_image = image.resize((new_width, new_height))

    square_image = Image.new('RGB', (size, size), (0, 0, 0))

    # 计算在正方形图像中居中的起始位置
    # x = (size - new_width) // 2
    # y = (size - new_height) // 2

    # square_image.paste(resized_image, (x, y))
    # square_image.show()
    square_image = ImageOps.pad(resized_image, (size, size))
    return square_image

# 从命令行获取参数
if len(sys.argv) < 4:
    print("请提供图片路径和输出路径作为命令行参数")
else:
    image_path = sys.argv[1]
    tjc_path = sys.argv[2]
    try:
        size = int(sys.argv[3])
    except ValueError:
        size = 200

    # start_time = time.time()
    convert_to_rgb565(image_path, tjc_path, size)
    # end_time = time.time()

    # run_time = end_time - start_time
    # print("程序运行时间 {run_time}", run_time, "秒")

