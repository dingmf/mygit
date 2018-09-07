from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from dj05app.models import MyUser

# Create your views here.
USER_PEER_PAGE_NUM = 5

def get_user_by_num(req, page_num):
    page_num = int(page_num)
    # 获取全部用户
    users = MyUser.objects.all()
    # 创建分页
    paginator = Paginator(
        users,
        USER_PEER_PAGE_NUM
    )
    # 参数校验
    if page_num <= 0 or page_num > paginator.num_pages:
        return HttpResponse("没数据了")
    # 拿到用户指定页面的那页数据
    page = paginator.page(page_num)
    data = {
        'users': page.object_list
    }
    return render(req, 'users.html', data)