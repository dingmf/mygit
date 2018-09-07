from django.conf.urls import url

from .views import get_person_by_bank, remove_person, remove_bank, get_engineer_by_desc, get_engineer_by_language

urlpatterns = [
    url(r'^get_person_by_bank/', get_person_by_bank),
    url(r'^remove_person/', remove_person),
    url(r'^remove_bank/', remove_bank),
    url(r"^get_engineer_by_desc/", get_engineer_by_desc),
    url(r'^get_engineer_by_language/', get_engineer_by_language)
]


