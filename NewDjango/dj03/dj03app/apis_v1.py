from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .my_util import send_verify_mail
from .models import *
from django.views.generic import View
from django.core.cache import cache

SUCCESS = 1
FAIL = 2

DATA = {
    'code': SUCCESS,
    'msg': 'ok',
    'data': ''
}

class RegisterAPI(View):
    def post(self, req):
        param = req.POST
        u_name = param.get("u_name")
        pwd = param.get("pwd")
        cpwd = param.get("cpwd")
        email = param.get("email")
        icon = req.FILES['icon']

#         队数据做校验
        if len(u_name) <=4:
            return HttpResponse("账号名过短")
        if pwd and len(pwd) > 0 and pwd == cpwd:
            if MyUser.objects.filter(username=u_name).exists():
                return HttpResponse("用户已存在")
            else:
                user = MyUser.objects.create_user(
                    username=u_name,
                    password=pwd,
                    email=email,
                    is_active=False,
                    icon=icon
                )
                token = send_verify_mail(email, req.grt_host())
                cache.set(token, user.id, settings.EMAIL_TOKEN_MAX_AGE)
                return redirect(reverse())





























