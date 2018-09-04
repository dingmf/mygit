from django.conf.urls import url
from .apis_v1 import *

urlpatterns = [
    url(r"^peotry$", PoetryAPI.as_view())
]
