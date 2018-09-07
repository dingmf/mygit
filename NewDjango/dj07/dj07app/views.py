from django.http import HttpResponse
from django.shortcuts import render
from .tasks import first_task, send_email
from .models import Poetry
from .my_singal import action

# Create your views here.

def first_celery(req):
    # 任务函数的异步调用
    first_task.delay(4)
    send_email.delay("3207196028@qq.com")
    return HttpResponse("好了")

def create_poetry(req):
    p = Poetry()
    p.title = "迷"
    p.author = "困"
    p.content = "锄禾日当午，码农真辛苦"
    p.save()
    action.send(sender="渣渣",paraml="o((>ω< ))o",param2="昂昂昂")
    return HttpResponse("搞定")