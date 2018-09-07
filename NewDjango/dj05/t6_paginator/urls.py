from django.conf.urls import url
from .views import get_user_by_num

urlpatterns = [
    url(r'^user/(\d+)', get_user_by_num)
]