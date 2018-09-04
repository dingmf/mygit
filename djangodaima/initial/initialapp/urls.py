from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^play$', play),
    url(r'^login$', my_login, name="login"),
    url(r'^myindex$', my_index),
    url(r'^logout$', my_logout, name="logout")

]
