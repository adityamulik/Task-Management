import json, os
import dj_database_url
import django_heroku
from django.core.exceptions import ImproperlyConfigured
from .base import *

DEBUG = False

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

SECRET_KEY = get_secret('SECRET_KEY')

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static Files

STATIC_ROOT = BASE_DIR("runtime", "static")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'