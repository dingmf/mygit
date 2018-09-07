from django.db.models.signals import pre_save, post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .my_singal import action

def pre_save_model(sender, **kwargs):
    print(sender)
    print(kwargs)

def post_save_func(sender, **kwargs):
    print('发送者',sender)
    print(kwargs)

pre_save.connect(pre_save_model)
post_save.connect(post_save_func)