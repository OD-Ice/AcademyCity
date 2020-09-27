import random
# Image: 是一个画板(context)，ImageDraw: 是一个画笔，ImageFont: 画笔的字体
from PIL import Image, ImageDraw, ImageFont
import time
import os
import string


# Captcha验证码
class Captcha:
    # 把一些常量抽取成类属性
    # 字体的位置
    font_path = os.path.join(os.path.dirname(__file__), 'iosevka-term-extrabolditalic.ttf')
    # font_path = 'utils\captcha\iosevka-term-lightoblique.ttf'
    # 生成几位数的验证码
    number = 4
    # 生成验证码图片的宽度和高度
    size = (100, 40)
    # 背景颜色，默认为白色 RGB(Re, Green, Blue)
    bgcolor = (0, 0, 0)
    # 验证码字体大小
    fontsize = 20
    # 是否加入干扰线
    draw_line = True
    # 是否加入噪点
    draw_point = True
    # 干扰线条数
    line_number = 3

    SOURCE = list(string.ascii_letters)
    for index in range(0, 10):
        SOURCE.append(str(index))

    # 用来随机生成一个字符串(包括英文和数字)
    # 定义成类方法，然后是私有的，对象在外面不能直接调用
    @classmethod
    def gene_text(cls):
        return ''.join(random.sample(cls.SOURCE, cls.number))

    # 用来绘制干扰线
    @classmethod
    def __gene_line(cls, draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        # 干扰线随机颜色
        linecolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.line([begin, end], fill=linecolor)

    # 用来绘制干扰点
    @classmethod
    def __gene_points(cls, draw, point_chance, width, height):
        chance = min(100, max(0, int(point_chance)))  # 控制在0到100之间，point_chance越大噪点出现机会越多
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point([w, h], fill=(0, 0, 0))

    # 生成验证码
    @classmethod
    def gene_code(cls):
        width, height = cls.size
        image = Image.new('RGBA', (width, height), cls.bgcolor)  # 创建面板
        font = ImageFont.truetype(cls.font_path, cls.fontsize)  # 验证码的字体
        draw = ImageDraw.Draw(image)  # 创建画笔
        text = cls.gene_text()  # 生成字符串
        font_width, font_height = font.getsize(text)
        # 随机字体颜色
        fontcolor = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        draw.text(((width - font_width) / 2, (height - font_height) / 2), text, font=font, fill=fontcolor)  # 填充字符串
        # 如果需要绘制干扰线
        if cls.draw_line:
            # 遍历line_number次，就是画line_number根线条
            for x in range(cls.line_number):
                cls.__gene_line(draw, width, height)
        # 如果需要绘制噪点
        if cls.draw_point:
            cls.__gene_points(draw, 10, width, height)

        return text, image

