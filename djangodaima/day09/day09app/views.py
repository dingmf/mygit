from django.http import HttpResponse
from django.shortcuts import render
from .tasks import first_task, send_email
from .models import Poetry
# Create your views here.
from .my_singal import action

def first_celery(req):
    # 任务函数的异步调用
    first_task(4)
    send_email.delay("3207196028@qq.com")
    return HttpResponse("ok")


def create_poetry_czn(req):
    p = Poetry()
    p.title = "当午"
    p.author = "萨弗迪"
    p.content = "锄禾日当午，汗滴禾下土"
    p.save()
    # 发送信号
    action.send(sender="123", paraml="321", param2="123456")
    return HttpResponse("搞定")

