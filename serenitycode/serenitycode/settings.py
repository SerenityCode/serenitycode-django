from .settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'serenitycode',
        'USER': 'jeff',
        'PASSWORD': 'pw',
        'HOST': 'localhost',
        'PORT': '',
    }
}