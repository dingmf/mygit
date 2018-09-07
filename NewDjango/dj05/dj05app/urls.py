from django.conf.urls import url
from .views import my_login, my_index, home, update_msg

urlpatterns = [
    url(r'^my_login$',my_login),
    url(r'^my_index$', my_index),
    url(r'^home$', home),
    url(r'^update$', update_msg)
]