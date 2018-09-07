import os
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .my_utils import get_random_str


# Create your views here.

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
            return redirect('/dj05app/my_index')
        else:
            return HttpResponse("用户名或者密码错误")


@login_required(login_url="/dj05app/my_login")
def my_index(req):
    user = req.user
    return render(req, 'index.html', {"u_name": user.username})

def home(req):
    res = ['美女荷官']
    return render(req, 'home.html', {'data': res})

@login_required(login_url="/dj05app/my_login")
def update_msg(req):
    user = req.user
    print(user.icon)
    if req.method == "GET":
        data = {
            'u_name': user.username,
            # 拿头像文件路径
            # 'icon': '/static/uploads/' + user.icon.url
            'icon': '/static/uploads/icons/hehe.jpg'
        }
        return render(req, 'person.html', data)
    else:
        '''
        # 拿文件
        icon = req.FILES['u_icon']
        # 赋值
        user.icon = icon
        # 保存
        user.save()
        # 拼接返回数据
        data = {
            'u_name': user.username,
            # 拿头像文件路径
            'icon': '/static/uploads/' + user.icon.url
        }
        print(user.icon)
        return render(req, 'person.html', data)
        '''

        #原生方法
        #拿文件数据
        icon = req.FILES['u_icon']
        print(icon.name)
        file_name = 'icons/' + get_random_str() + ".jpg"
        # 拼接一个自己的文件路径
        print(file_name)
        image_path = os.path.join(settings.MEDIA_ROOT, file_name)
        #打开拼接的文件路径
        with open(image_path, 'wb')as fp:
            #遍历图片的块数据\
            for i in icon.chunks():
                # 将图片数据 写入自己的那个文件
                fp.write(i)
        print(image_path)
        # 拼接返回数据
        data = {
            'u_name': user.username,
            # 拿头像文件路径
            'icon': '/static/uploads/' + file_name
        }
        print(user.icon)
        return render(req, 'person.html', data)
