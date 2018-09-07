from django.conf.urls import url
# from .apis_v1 import *
from .apis_v1 import PoetryAPI

urlpatterns = [
    url(r"^peotry$", PoetryAPI.as_view())
]