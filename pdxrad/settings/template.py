from base import *

DEBUG = True

ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT = False



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'mysql.example.com',
        'PORT': '',
    }
}

#Email Options
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'mail.example.com'
EMAIL_HOST_USER = 'admin@example.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'admin@example.com'

#Media
MEDIA_ROOT = '/home/user/media/'
MEDIA_URL = '/media/'


STATIC_URL = '/static/'
CKEDITOR_UPLOAD_PATH = "uploads/"
