from django.conf.urls import url
from .views import get_humen_list, cates, catel,cate_filter, get_goods_by_datetime, get_count, get_player, \
    get_player_by_q, create_play, my_login, index, home, update_msg, my_register, active

urlpatterns = [
    url(r'^get_humen_list/', get_humen_list),
    url(r'^cates/', cates),
    url(r'^catel/', catel),
    url(r'^cate_filter/', cate_filter),
    url(r'^get_count_t/', get_count),
    url(r'^get_goods_by_datetime$',get_goods_by_datetime),
    url(r'^get_player$', get_player),
    url(r'^get_player_by_q/', get_player_by_q),
    url(r'^create_play/', create_play),
    url(r'^my_login/', my_login,name='my_login'),
    url(r'^index/', index, name='index'),
    url(r'^home$', home),
    url(r'^active/', active),
    url(r"^update$", update_msg),
    url(r'^my_register$', my_register,name='my_register')
]