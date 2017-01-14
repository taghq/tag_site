import os, sys

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a$mnnxmi)6x^lply@gnwm^g-=2wpbg7yjn$17i1gghl+02yqs9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}


####Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'neurobomber@gmail.com'
EMAIL_HOST_PASSWORD = 'SantaCruz2010'
DEFAULT_FROM_EMAIL = 'neurobomber@gmail.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'pdxrad', 'static'),
)
SITE_ID = 1
