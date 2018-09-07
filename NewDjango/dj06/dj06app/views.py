import random
import io
from PIL import ImageDraw
from PIL import ImageFont
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail, send_mass_mail
from django.views.decorators.cache import cache_page
from .my_util import get_random_color, get_random_str
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import time
from time import ctime
from django.template import loader
import logging
logger = logging.getLogger('django')

# Create your views here.

def get_verify_img(req):
    # 画布背景颜色
    bg_color = get_random_color()
    # 画布大小
    img_size = (130, 70)
    # 定义画布
    image = Image.new("RGB", img_size, bg_color)
    # 定义画笔
    draw = ImageDraw.Draw(image, "RGB")
    # 设置文字颜色
    # text_color = (255, 0, 0)
    # 创建字体
    font_path = '/home/ubuntu/gz1803/Newdjango/dj06/static/fonts/ADOBEARABIC-BOLDITALIC.OTF'
    # 实例化字体  并指定大小是30
    font = ImageFont.truetype(font_path, 30)
    # 准备圆字符集
    source = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
    # 保存每次随机出来的字符
    code_str = ""
    for i in range(4):
        # 获取数字随机颜色
        text_color = get_random_color()
        # 获取随机数字
        tmp_num = random.randrange(len(source))
        # print(tmp_num)
        # 获取随机字符
        random_str = source[tmp_num]
        # 将每次随机的字符保存（遍历）
        code_str += random_str
        # 将字符画到画布上
        draw.text((10 + 30*i, 20), random_str, text_color, font)

    # 记录给哪个请求发了什么验证码
    req.session['code'] = code_str
    print(code_str)

    # 使用画笔将文字画到画布上
    # draw.text((10, 20), "X", text_color, font)
    # draw.text((40, 20), "Q", text_color, font)
    # draw.text((60, 20), "W", text_color, font)
    # 获得一个缓存区
    buf = io.BytesIO()
    # 将图片保存到缓存区
    image.save(buf, 'png')
    # 将缓存区的内容返回给前端  .getvalue把缓存区的所有数据读取
    return HttpResponse(buf.getvalue(), 'image/png')

def login_api(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        params = req.POST
        # 用户输入的
        code = params.get("verify_code")
        # 从session获取的
        server_code = req.session.get("code")
        print(server_code)
        # 做判断比较
        if server_code.lower() == code.lower():
            return HttpResponse("验证成功")
        else:
            return HttpResponse('输入验证码错误')

# 过期缓存时间
@cache_page(60)
def get_data(req):
    # 缓存时间
    time.sleep(5)
    return HttpResponse("1234")

def get_html(req):
    return render(req, 'get_html.html')

@cache_page(10)
def test(req):
    now = ctime()
    return render(req, 'test.html', {'now':now})

def send_my_email(req):
    title = "美团骑手offer"
    msg = "恭喜你成为美团骑手"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '3207196028@qq.com'
    ]
    # 发送邮件
    send_mail(title, msg, email_from, reciever)
    return HttpResponse("ok")

def send_email_v1(req):
    title = "美团骑手offer"
    msg = " "
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '3207196028@qq.com'
    ]
    # 加载模板
    template = loader.get_template('email.html')
    # 渲染模板
    html_str = template.render({"msg": "123456"})
    print(html_str)
    # 发送邮件
    send_mail(title, msg, email_from, reciever, html_message=html_str)
    return HttpResponse("ok")

def verify(req):
    if req.method == "GET":
        return render(req, 'verify.html')
    else:
        param = req.POST
        email = param.get('email')
        # 生成随机字符
        random_str = get_random_str()
        # 拼接验证链接（加网址）
        url = "http://118.24.95.20:8000/dj06app/active/" + random_str
        # 加载激活模板
        tmp = loader.get_template('active.html')
        # 渲染
        html_str = tmp.render({'url': url})

        title = "美团骑手offer"
        msg = " "
        email_from = settings.DEFAULT_FROM_EMAIL
        reciever = [
            # '3207196028@qq.com'
            email,
        ]
        send_mail(title, msg, email_from, reciever, html_message=html_str)
        # 记录 token 对应的邮箱是谁 v  k
        cache.set(random_str, email, 120)
        return HttpResponse('ok')

def active(req, random_str):
    # 拿参数对应的缓存数据
    res = cache.get(random_str)
    if res:
        # 通过邮箱找到对应用户
        # 给用户的状态字段做更新，从未激活变成激活状态
        return HttpResponse(res+"激活成功")
    else:
        return HttpResponse("验证链接无效")

def send_many_email(req):
    title = "美团骑手offer"
    content1 = "该点外卖啦"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever1 = [
        '3207196028@qq.com',
        '928620803@qq.com',
        '1179109710@qq.com',
    ]
    content2 = "吃饭睡觉不想敲代码"
    # 邮件1
    msg1 = (title, content1, email_from, reciever1)
    # 邮件2
    msg2 = ("渣渣们", content2, email_from, ['928620803@qq.com', '1179109710@qq.com'])
    send_mass_mail((msg1,msg2), fail_silently=True)
    return HttpResponse("发送好了")

def test_log(req):
    logger.info("要下课了")
    return HttpResponse("好开心")