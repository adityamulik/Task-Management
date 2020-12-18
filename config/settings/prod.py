import json, os
from django.core.exceptions import ImproperlyConfigured
from .base import *

DEBUG = True

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

SECRET_KEY = get_secret('SECRET_KEY')

# Static Files

STATIC_ROOT = BASE_DIR("runtime", "static")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'