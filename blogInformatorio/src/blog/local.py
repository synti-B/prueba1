from .settings import *


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'configuracion',
        'USER': 'root',
        'PASSWORD':'caramelo7',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}