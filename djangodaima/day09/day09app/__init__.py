from django.db.models.signals import pre_save, post_save
from django.core.signals import request_finished
from django.dispatch import receiver

from .my_singal import action

def pre_save_model(sender, **kwargs):
    print(sender)
    print(kwargs)

def post_save_func(sender, **kwargs):
    print('发送者', sender)
    print(kwargs)


pre_save.connect(pre_save_model)
post_save.connect(post_save_func)

@receiver(request_finished)
def test_finished_func(sender, **kwargs):
    print("被调用")

def my_design(sender, **kwargs):
    print("自定义信号被调用")
    print(sender)
    print(kwargs)

action.connect(my_design)


