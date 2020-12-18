import json, os
import dj_database_url
import django_heroku
from django.core.exceptions import ImproperlyConfigured
from .base import *

DEBUG = False

SECRET_KEY = '&**mifsw3@hi_1an=!o76li#^av!#z2f3k4=5!9qohf%$)n6ke'

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'USER': '<user_name>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# Static Files

# STATIC_ROOT = BASE_DIR("runtime", "static")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_USE_FINDERS = True