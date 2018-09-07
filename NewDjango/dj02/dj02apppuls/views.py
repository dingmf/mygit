from django.http import HttpResponse
from django.shortcuts import render
from dj02apppuls import models

# Create your views here.

def get_person_by_bank(req):
    bank = models.BankCard.objects.all().first()
    print(type(bank))
    return HttpResponse(bank.person)

def remove_person(req):
    person = models.Person.objects.all().last()
    person.delete()
    return HttpResponse("删除成功")

def remove_bank(req):
    bank = models.BankCard.objects.all().last()
    bank.delete()
    return HttpResponse("删除成功了")


def get_engineer_by_desc(req):
    engineer = models.Engineer.objects.filter(
        language__desc__contains="从入门到放弃"
    )
    return HttpResponse(engineer)

def get_engineer_by_language(req):
    # 先拿到id为2的语言
    my_python = models.Language.objects.get(id=1)
    # 获取会python的工程师
    res = my_python.engineer_set.all()
    return HttpResponse(res)

