from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^verify_img", get_verify_img),
    url(r"^login", login_api),
    # url(r"^get_data$", get_data),
    # url(r"^get_players$", get_players),
    # url(r"^rich$", get_html)
]