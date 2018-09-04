from django.forms import model_to_dict

from .models import Poetry
from  django.http import JsonResponse
from django.views.generic import View

SUCCESS = 1

DATA = {
    'code': SUCCESS,
    'msg': 'ok',
    'data': ""
}

class PoetryAPI(View):
    def get(self, request):
        p_id = request.GET.get("p_id")
        data = Poetry.objects.get(pk=p_id)
        DATA['data'] = model_to_dict()
        return JsonResponse(DATA)

    def post(self, req):
        params = req.POST
        p_title = params.get("title")
        p_author = params.get("author")
        p_content = params.get("content")
#         创建数据
        p = Poetry.objects.create(
            title = p_title,
            author = p_author,
            content = p_content
        )
        DATA['data'] = p.id
        return JsonResponse(DATA)


