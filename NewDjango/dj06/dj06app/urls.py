from django.conf.urls import url

from .views import get_verify_img, \
    login_api, \
    get_data, \
    get_html, \
    test, \
    send_my_email, \
    send_email_v1,\
    verify, active,\
    send_many_email,\
    test_log


urlpatterns = [
    url(r'^get_verify_img', get_verify_img),
    url(r'^login', login_api),
    url(r'^get_data$', get_data),
    url(r'^get_html$', get_html),
    url(r'^test$', test),
    url(r'^send_my_email$', send_my_email),
    url(r'^send_email_v1$', send_email_v1),
    url(r'^verify$', verify),
    url(r"^active/(.+)", active),
    url(r'^send_many_email$', send_many_email),
    url(r"^test_log$", test_log)
]