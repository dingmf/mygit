from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.mail import send_mail
from django.db.models import Q
from django.db.models import Sum, F
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.conf import settings
import uuid
import hashlib
from django.urls import reverse

from .models import Person, Category, Goods, Team, Player, MyUser


# Create your views here.

def my_register(req):
    if req.method == "GET":
        return render(req, "my_register.html")
    else:
        params = req.POST
        u_name = params.get("u_name")
        email = params.get("email")
        phone = params.get("phone")
        pwd = params.get("pwd")
        cpwd = params.get("cpwd")
        icon = req.FILES['u_icon']
        print(u_name,pwd,cpwd)
        # random_str = get_random_str()
        # 判断用户的输入是否满足基本要求
        if u_name and len(u_name) > 6 and pwd and cpwd and pwd == cpwd:
            # 判断用户是否已经被注册
            exists_flag = MyUser.objects.filter(username=u_name).exists()
            if exists_flag:
                return HttpResponse("该用户被注册")
            else:
                # 如果没有被注册，那么就创建用户
                user = MyUser.objects.create_user(username=u_name, email=email, password=pwd, phone=phone)
                # 生成随机字符
                random_str = get_str()
                # 拼接验证连接
                url = "http://118.24.95.20:8000/dj02app/active/" + random_str
                # 加载激活模板
                tmp = loader.get_template('active.html')
                # 渲染
                html_str = tmp.render({'url': url})
                print(html_str)

                # 准备邮箱数据
                title = "邮箱验证"
                msg = ""
                email_from = settings.DEFAULT_FROM_EMAIL
                reciever = [
                    email,
                ]
                send_mail(title, msg, email_from, reciever, html_message=html_str)
                cache.set(random_str, email, 120)
                user.icon = icon
                user.save()
                return render(req, 'login.html')
        else:
            return HttpResponse("账号密码格式错误")
def get_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()

def active(req, token):
    # 在缓存尝试拿数据
    user_id = cache.get(token)
    if user_id:
        # 如果拿到用户 那就修改用户的激活状态
        MyUser.objects.filter(pk=int(user_id)).update(is_active=True)
        return HttpResponse("激活成功")
    else:
        return HttpResponse("链接不正确或失效")




def my_login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        params = req.POST
        u_name = params.get('u_name')
        pwd = params.get('pwd')
        # 数据校验
        # 用户校验
        user = authenticate(username=u_name, password=pwd)
        if user:
            # 用户登录
            login(req, user)
            # 登录成功返回页面
            return redirect('/dj02app/index/')
        else:
            return HttpResponse('用户名或密码错误')


@login_required(login_url='/dj02app/login/')
def index(req):
    user = req.user
    return render(req, 'index.html', {'u_name': user.username})


def home(req):
    res = ['澳门赌场上线啦，性感荷官在线发牌']
    return render(req, 'home.html', {'data': res})


@login_required(login_url='/dj02app/login/')
def update_msg(req):
    user = req.user

    print(user.icon)
    if req.method == 'GET':
        data = {
            'u_name': user.username,
            'icon': '/static/uploads/' + user.icon.url
        }
        return render(req, 'active.html', data)
    else:
        icon = req.FILES['u_icon']
        user.icon = icon
        user.save()
        data = {
            'u_name': user.username,
            'icon': '/static/uploads/' + user.icon.url
        }
        print(user.icon)
        return render(req, 'active.html', data)
















def get_humen_list(req):
    persons = Person.objects.all()
    return render(req, 'p_list.html', context={'data': persons})


def cates(req):
    # result = Category.objects.all()
    # result = Category.objects.filter(id=1)
    result = Category.objects.all().order_by("-id")
    return render(req, 'cates.html', {'res': result, 'title': '分类列表'})


def catel(req):
    print(req)
    print(dir(req))
    return HttpResponse("haha")


def cate_filter(req):
    key_world = req.GET.get("kw")
    res = Category.objects.filter(desc__contains=key_world)
    print(res)
    return HttpResponse(res)


def get_goods_by_datetime(req):
    my_time = req.GET.get("time")
    res = Goods.objects.filter(id_datetime__year=my_time)
    return HttpResponse(res)


def get_count(req):
    # 拿全部的数据
    players = Player.objects.all()
    res = players.aggregate(Sum('count'))
    print(res)
    # return HttpResponse(result.get('count__sum'))
    return HttpResponse('ok')


def get_player(req):
    res = Player.objects.filter(age__gt=F('count'))
    # 将查询出来的对象 全部转化成数组嵌套字段的格式
    result = [model_to_dict(i) for i in res]
    print(result, type(result))
    return HttpResponse(res)


def get_player_by_q(req):
    #     需求：查询年纪大于20 活力大于70的
    res = Player.objects.filter(Q(age__gt=20) | Q(count=100))
    return HttpResponse(res)


def create_play(req):
    player = Player.my_objects_one.create_play()
    return HttpResponse("创建了一个叫{name}".format(name=player.name))
