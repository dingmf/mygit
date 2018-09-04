import time
from django.shortcuts import render
from django.http import HttpResponse
# from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from django.views.decorators.cache import cache_page

from .my_util import get_random_color
import os
import io
import random

# Create your views here.

def get_verify_img(req):
    # 画布背景颜色
    bg_color = get_random_color()
    img_size = (130, 70)
    # 实例一个画布
    image = Image.new("RGB", img_size, bg_color)
    # 实例化一个画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 设置文字的颜色
    # text_color = (255, 0, 0)
    # 创建字体
    font_path = "/home/ubuntu/gz1803/codes/day06/static/fonts/ADOBEARABIC-BOLDITALIC.OTF"
    font = ImageFont.truetype(font_path, 30)
    source = "abcdefghijkionmopqrstQWERTYUIOPADGFHZJCKVLBVNBM1234567890"

    # 保持每次随出来的字符
    code_str = ""
    for i in range(4):
        text_color = get_random_color()
        # 获取随机数字
        tmp_num = random.randrange(len(source))
        # 获取随机字符
        random_str = source[tmp_num]
        code_str +=random_str
        draw.text((10 + 30*i, 20), random_str, text_color, font)

    # 记录给哪个请求发了什么验证码
    req.session['code'] = code_str

    # draw.text((30, 20), "X", text_color)
    # draw.text((40, 20), "z", text_color)
    # draw.text((60, 20), "9", text_color)


    # 获得一个缓冲区
    buf = io.BytesIO()
    # 将图片保存到缓冲区
    image.save(buf, 'png')
    # 将缓冲区的内容 返回给前端
    return HttpResponse(buf.getvalue(), 'image/png')


def login_api(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        params = req.POST
#         用户输入的
        code = params.get("verify_code")
#         从session获取的
        server_code = req.session.get("code")
#         做判断比较
        if server_code.lower() == code.lower():
            return HttpResponse("ok")
        else:
            return HttpResponse("fail")

@cache_page(60)
def get_data(req):
#     假装在加载数据库
    time.sleep(5)
    return HttpResponse("睡醒了")

