from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os

# 设置系统的环境配置用的是Django
os.environ.setdefault('DJANGO_SETTING_MODEULE','dj08.settings')

# 实例化celery
app = Celery('mycelery')

# APP设置时区
app.conf.timezone = 'Asia/Shanghai'

# 指定celery的配置来源  用的是项目的配置文件settings.py
app.config_from_object('django.conf:settings')

# 让celery自动去发现我们的任务（task）
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)
# 你需要在app目录下新建一个叫tasks.py(不能写错) 文件