from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: Generate Secret Key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.scheding.com.au']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Media urls

# MEDIA_URL needs to be like this so that relative paths work properly for uploaded images in the blog
MEDIA_URL = 'http://www.scheding.com.au/media/'
MEDIA_ROOT = '/var/www/scheding.com.au/media/'
