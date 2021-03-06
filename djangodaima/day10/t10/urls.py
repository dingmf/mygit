from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^home$", home, name='home'),
    url(r"^market/(\d+)/(\d+)", market, name='market'),
    url(r"^cart$", cart, name='cart'),
    url(r"^mine$", mine, name='mine'),
    url(r"^register$", register_view, name="register"),
    url(r"^login$", my_login, name="login_view")
]