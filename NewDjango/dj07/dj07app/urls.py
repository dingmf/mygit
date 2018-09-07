from django.conf.urls import url

from .views import first_celery, create_poetry

urlpatterns = [
    url(r'^first_celery$', first_celery),
    url(r'^create_poetry$', create_poetry),
]