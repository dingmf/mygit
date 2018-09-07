from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^work$", work),
    url(r"^index$", index),
    url(r"^response_index$", response_index),
    url(r"^get_josn$", get_josn),
    url(r"^play$", play),
    url(r"^my_login$", my_login, name="login"),
    url(r"^my_index$", my_index),
    url(r"^logout$", my_logout, name="loginout"),
    url(r"^myregister$", register),
    url(r"^myloginv1$", my_login_v1),
    url(r"^new_index$", new_index),
    url(r"^new_logout$", new_logout, name="new_logout")
]