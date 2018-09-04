from django.conf.urls import url
from .apis_v1 import RegisterAPI,LoginAPI,active, LogoutAPI

urlpatterns = [
    url(r"^register$", RegisterAPI.as_view(), name="api_register"),
    url(r"^active/(.+)", active),
    url(r"^login$", LoginAPI.as_view()),
    url(r"^logout", LogoutAPI.as_view(), name="logout")
]