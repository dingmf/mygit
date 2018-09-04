# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def hello_func(req):
#     return HttpResponse("123456")
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
def hello_func(req):
    return HttpResponse("<h1>外焦里嫩的老师来报答</h1>")

def get_html(request):
    return render(request, "humen.html")

def get_humen_list(req):
    # 拿到gz01_person那个表的全部数据
    persons = Person.objects.all()
    return render(req, "p_list.html", context={'data': persons})