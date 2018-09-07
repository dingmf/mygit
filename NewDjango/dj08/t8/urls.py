from django.conf.urls import url

from .views import first_celery

urlpatterns = [
    url(r'^first_celery$', first_celery)
]