from .base import *

DEBUG = True
PRODUCTION = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432'
    }
}

FACEBOOK_APP_ID = data['FACEBOOK_APP_ID_SANDBOX']
FACEBOOK_APP_SECRET = data['FACEBOOK_APP_SECRET_SANDBOX']
FACEBOOK_REDIRECT_URI = data['FACEBOOK_REDIRECT_URI_SANDBOX']
