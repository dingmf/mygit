from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
def work(req):
    return render(req, 'work.html')

def index(req):
    # 请求的ip，不是自己的
    print(req.get_host())
    # 类似字典的参数，包含了get的所有参数
    print(req.GET)
    # COOKIES 类似字典的参数，包含所有的COOKIE
    print(dir(req.COOKIES))
    # 请求完整路径
    print(req.path)
    # 编码方式，常用utf-8
    print(req.encoding)
    # 请求的方式，常见DET，POST
    print(req.method)
    print(req.META.get('REMOTE_ADDR'))
    return HttpResponse("ok")

def response_index(req):
    response = HttpResponse()
    response.content = "content设置的"
    # 追加
    response.write("我是write写的")
    # 直接覆盖
    response.content = "素质是有点"
    # 冲刷缓冲区
    response.flush()
    response.status_code = 404
    return response

def get_josn(req):
    data = [1,2,3,45]
    return JsonResponse({"data":data})

def play(req):
    return render(req, '2048.html')

def my_login(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        params = req.POST
        name = params.get("u_name")
        response = HttpResponse()
        # 设置cookies
        response.set_cookie('u_name', name, max_age=5)
        # 设置session
        req.session["ll"] = name
        response.content = '登录成功'
        return response

def my_index(req):
    # 拿cookies里面的值，返回给页面
    u_name = req.COOKIES.get("u_name")
    # 读取session
    my_session_data = req.session.get('ll')
    print(my_session_data)
    return render(req, 'index.html',{'u_name':u_name})


def my_logout(req):
    # 重定向到首页
    response = HttpResponseRedirect("/dj04app/my_index")
    # 删除u_name 对于的cookies
    response.delete_cookie('u_name')
    return response


def register(req):
    if req.method == 'GET':
        return render(req, "register.html")
    else:
        params = req.POST
        u_name = params.get("u_name")
        pwd = params.get("pwd")
        confirm_pwd = params.get("confirm_pwd")
        # 判断用户输入是否满足基本条件
        if u_name and len(u_name)>3 and pwd and confirm_pwd and pwd == confirm_pwd:
            # 判断用户名是否被注册过
            exists_flag = User.objects.filter(username=u_name).exists()
            if exists_flag:
                return HttpResponse("该用户已被注册")
            else:
                # 创建用户
                # user = User.objects.create_user(username=u_name,password=pwd)
                User.objects.create_user(username=u_name,password=pwd)
                # return HttpResponse("创建了" + user.username)
                return render(req, "my_login.html")
        else:
            return HttpResponse("账号密码不正确")

def my_login_v1(req):
    if req.method == "GET":
        return render(req, 'my_login.html')
    else:
        # 拿参数
        params = req.POST
        u_name = params.get("u_name")
        pwd = params.get("pwd")
        # 校验数据格式
        if u_name and len(u_name)>3 and pwd and len(pwd)>=3:
            # 校验用户
            user = authenticate(username=u_name, password=pwd)
            print(user)
            if user:
                # 通过校验的用户 让其登录
                login(req, user)
                return render(req, "new_index.html", {"u_name": user.username})
            else:
                # 没通过的  返回错误
                return HttpResponse("账号或密码错误")
        else:
            return HttpResponse("请补全信息")

def new_index(req):
    print(dir(req))
    user = req.user
    print(user)
    return render(req, "new_index.html", {"u_name": user.username})

def new_logout(req):
    logout(req)
    # return redirect('new_index')
    # return render(req, "register.html")
    # 重定向到首页
    response = HttpResponseRedirect("/dj04app/myregister")
    # 删除u_name 对于的cookies
    response.delete_cookie('u_name')
    return response