"""
Django settings for web_demo project.

Generated by 'django-admin startproject' using Django 1.8.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j4^0nhh*_0!1)-0h)iu+93ajfdazj0ep@)-!dho@air8zr!rj6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'demo_test',
    'business_site',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'web_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'web_demo.wsgi.application'


# AUTH_USER_MODEL = 'business_site.User'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #数据库引擎
        'NAME': 'busi',                       #数据库名
        'USER': 'root',                       #用户名
        'PASSWORD': 'password',                   #密码
        'HOST': 'localhost',                           #数据库主机，默认为localhost 172.17.34.127
        'PORT': '3306',                           #数据库端口，MySQL默认为3306
        'OPTIONS': {
            'autocommit': True,
        },
    }
}
# ##缓存配置，使用文件系统来做缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache', #路径
#         'TIMEOUT': 600,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Beijing'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
("css", os.path.join(STATIC_ROOT, 'css')),
("js", os.path.join(STATIC_ROOT, 'js')),
("images", os.path.join(STATIC_ROOT, 'images')),
("bootstrap", os.path.join(STATIC_ROOT, 'bootstrap')),
)

#上传文件设置
MEDIA_ROOT = os.path.join(BASE_DIR, 'business_site/media/')
MEDIA_URL =  '/media/'

