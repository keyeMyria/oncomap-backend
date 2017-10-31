from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

FORCE_SCRIPT_NAME = '/api'

ALLOWED_HOSTS = ['localhost:8000']

SITE_URL = 'http://localhost:8000/api/'


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DB_NAME', 'omicsmap'),
        'USER': os.environ.get('DB_USER', 'onconet'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'onc0n3t'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

