from django.conf.urls import url
from .views import (get_teachers,
                    get_teachers_v1,
                    get_stu,
                    index,
                    get_teacher
                    )

urlpatterns = [
    url(r'^teachers$',get_teachers),
    url(r'^teachers-v1$',get_teachers_v1),
    url(r'^jjstu$', get_stu, name="dmf"),
    url(r'^index$', index),
    url(r'^teacher/(\d+)', get_teacher, name="zhangsan")
]