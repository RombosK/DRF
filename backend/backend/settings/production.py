from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'backend',
        'USER': 'superadmin',
        'PASSWORD': 'superadmin',
        'HOST': 'db',
        'PORT': '5432',
    }
}





