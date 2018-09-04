from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import Teacher

# Create your views here.

def get_teachers(req):
    result = Teacher.objects.all()
    return render(
        req,
        'teachers.html',
        context={'teachers': result})

def get_teachers_v1(req):
    # 加载模板
    template = loader.get_template('teachers.html')
    # print(template)
    # print(dir(template))
    # 拿数据
    result = Teacher.objects.all()
    # 渲染模板，同时加入数据
    template_str = template.render({'teachers':result})
    print(template_str)
    # 将渲染得到的html字符串返回给请求
    return HttpResponse(template_str)

def get_stu(req):
    res = Teacher.objects.all()
    msg = '<p>dd</p>'
    msg1 = "<script>alert('页面被占领')</script>"
    return render(req, 'stu_2.html', {'teachers': res, 'msg':msg})

def index(req):
    return HttpResponseRedirect(reverse('python1803:zhangsan', args=(1, )))

def get_teacher(req, t_id):
    res = Teacher.objects.get(pk=t_id)
    return HttpResponse(res)










