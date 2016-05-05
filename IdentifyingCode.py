# coding=utf-8
import random
import string
import math
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# 字体的位置
font_path = '/System/Library/Fonts'

# 生成验证码的位数
number = 4

# 生成验证码的宽度和高度
size = (110, 40)

# 背景颜色
bgcolor = (255, 255, 255)

# 字体颜色
fontcolor = (0, 0, 255)

# 干扰线颜色
linecolor = (0, 255, 0)

# 是否加入干扰线
draw_line = True

# 加入干扰线条数上限
line_number = (1, 8)


# 随机生成一个字符串
def gene_test():
    source = list(string.letters)
    for index in range(0, 10):
        source.append(str(index))
    return ''.join(random.sample(source, number))    # number是生成验证码的位数


# 绘制干扰线
def gene_line(draw, width, height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=linecolor)


# 生成验证码
def gene_code():
    width, height = size    # 宽和高
    image = Image.new('RGBA', (width, height), bgcolor)    # 创建图片
    font = ImageFont.truetype(font_path, 25)    # 验证码字体
    draw = ImageDraw.Draw(image)    # 创建画笔
    text = gene_test()    # 生成字符串
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / number, (height - font_height) / number), text, font = font, fill=fontcolor)
    if draw_line:
        gene_line(draw, width, height)
    image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0),Image.BILINEAR)   # 创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)    # 滤镜，边角加强
    image.save('idencode.png')    # 保存验证码图片
if __name__ == "__main__":
    gene_code()