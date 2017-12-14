from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tv_server',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD':'123456',
    }
}

ALLOWED_HOSTS = ['192.168.80.190','127.0.0.1']