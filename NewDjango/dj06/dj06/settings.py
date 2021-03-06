"""
Django settings for dj06 project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from os import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&yta%x_cu771#-fasnuacpsmvzz1-n3&dp4ax0@w!buszvbl7^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dj06app',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj06.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dj06.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_06',
        'HOST': '118.24.95.20',
        'PORT': '3306',
        'USER': environ.get('DBUSER'),
        'PASSWORD': environ.get('DBPWD')
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#         'TIMEOUT': '60',
#         'OPTIONS': {
#             # 最大缓存个数（默认300）
#             'MAX_ENTRIES': '300',
#         },
#         'KEY_PREFIX': 'rock',
#         'VERSION': '1',
#     }
# }

# 富文本
TINYMCE_DEFAULT_CONFIG = {
    # 主题
    'theme': 'advanced',
    # 宽
    'width': 800,
    # 高
    'height': 600,
}

# 邮件配置
EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.qq.com'  # 如果是 163 改成 smtp.163.com

EMAIL_PORT = 465

EMAIL_HOST_USER = environ.get("EMAIL_SENDER") # 帐号

EMAIL_HOST_PASSWORD = environ.get("EMAIL_PWD")  # 授权码（****）
# 默认邮件
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 日志
ADMINS = (
    ('tom', '*******@163.com'),
)
LOGGING = {
    'version': 1,
    # 是否覆盖之前的log
    'disable_existing_loggers': False,
    # 格式设置
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    # 过滤条件 什么时候生效
    'filters': {
        # 线上部署需要注意
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    # 指定你的日志输出到哪里
    'handlers': {
        'null': {
            'level': 'DEBUG', #log.info() 设置级别
            'class': 'logging.NullHandler', # 使用那个类
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "log", 'debug.log'),  # 文件路径
            'maxBytes': 1024 * 1024 * 5, # 一个文件存多少内容
            'backupCount': 5, #可以有5个 5兆的日志文件
            'formatter': 'standard', # 使用的格式
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler', #输出终端
            'formatter': 'standard',
        },
    },
    # 写几个  提供给大家用log
    'loggers': {
        'django': {
            'handlers': ['console', 'debug'], #指定输出的位置
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['debug', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True, #是否继承父类的log信息
        },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}

