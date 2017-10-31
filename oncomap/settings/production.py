from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['oncoapi.biotektools.org']

SITE_URL = 'http://oncoapi.biotektools.org/'
STATIC_URL = '/static/'
STATIC_ROOT = '/home/serendipity/webapps/oncomap_static/'
STATICFILES_DIRS = [

]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DB_NAME', 'omicsmap'),
        'USER': os.environ.get('DB_USER', 'onconet'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'onc0n3t'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
    }
}

CORS_ORIGIN_ALLOW_ALL = True   