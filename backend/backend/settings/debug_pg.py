from .debug import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'backend',
        'USER': 'superadmin',
        'PASSWORD': 'superadmin',
        'HOST': '127.0.0.1',
        'PORT': '54328',
    }
}
