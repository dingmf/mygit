from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import response
from django.shortcuts import render

# Create your views here.

def play(req):
    return render(req, '2048.html')

def my_login(req):
    if req.method == "GET":
        return render(req, 'login.html')
    else:
        params = req.POST
        name = params.get("name")
#         校验
        response = HttpResponse()
        response.set_cookie('u_name', name)
        # 设置session
        req.session['ll'] = name
        response.content = '登录成功'
        return response

def my_index(req):
    # 拿cookies里面的值
    u_name = req.COOKIES.get("u_name")
    # 读取session
    my_seesion_data = req.session.get("ll")
    print(my_seesion_data)
    return render(req, 'index.html', {'u_name': u_name})

def my_logout(req):
    # 重定向到首页
    response = HttpResponseRedirect("/t5/my_index")
    # 删除u_name对应的cookie
    response.delete_cookie('u_name')
    return response


