import json
import os
import redis
from os.path import abspath, join, dirname

BASE_DIR = abspath(join(dirname(abspath(__file__)), '..', '..', '..'))

data_path = os.path.join(BASE_DIR, 'designhubz/designhubz/settings/data.json')
data = json.loads(open(data_path).read())

LOGIN_URL = '/auth/login/'

ALLOWED_HOSTS = data['ALLOWED_HOSTS']
SECRET_KEY = data['SECRET_KEY']
DB_NAME = data['DB_NAME']
DB_USER = data['DB_USER']
DB_PASSWORD = data['DB_PASSWORD']
DB_HOST = data['DB_HOST']
SERVER_IP = data['SERVER_IP']

FACEBOOK_APP_ID = data['FACEBOOK_APP_ID']
FACEBOOK_APP_SECRET = data['FACEBOOK_APP_SECRET']
FACEBOOK_REDIRECT_URI = data['FACEBOOK_REDIRECT_URI']

BACKEND_DOMAIN = 'api.designhubz.co'
BACKEND_URL = 'http://api.designhubz.co'
FRONTEND_DOMAIN = 'designhubz.co'
FRONTEND_URL = 'http://designhubz.co'

AUTH_USER_MODEL = 'web.User'
APPEND_SLASH = False

DEFAULT_FROM_EMAIL = 'noreply@designhubz.co'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'django_mptt_admin',
    'rest_framework',
    'corsheaders',
    'web',
    'chat',
    'file',
    'project'
)

MIDDLEWARE = (
    'web.middleware.AccessControlMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'web.middleware.ActiveUserMiddleware'
)

ROOT_URLCONF = 'designhubz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'designhubz.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = BASE_DIR + '/static/media/'
STATIC_URL = '/static/'
MEDIA_URL = '/static/media/'

FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)

FILE_UPLOAD_TEMP_DIR = MEDIA_ROOT + 'tmp/'

STATICFILES_DIRS = [join(BASE_DIR, 'static')]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_PERMISSION_CLASSES': (),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'designhubz.authentication.BasicAuthentication',
        'designhubz.authentication.SessionAuthentication',
        'designhubz.authentication.TokenAuthentication'
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S',
    'EXCEPTION_HANDLER': 'web.exceptions.custom_exception_handler'
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d \
            %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {
        'console': {
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'db': {
            'class': 'designhubz.loggers.MyDbLogHandler',
            'formatter': 'verbose'
        }
    },

    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': True,
        },

        'django.request': {
            'handlers': ['db'],
            'level': 'ERROR',
            'propagate': False,
        },

        'app': {
            'level': 'DEBUG',
            'handlers': ['console', 'db'],
            'propagate': False,
        }
    }
}

# Custom token auth.
TOKEN_EXPIRE_MINUTES = 1400

REDIS_DB = redis.StrictRedis(host='127.0.0.1', port=6379, db=2)

TEST_CLIENT_EMAIL = 'vladigris@gmail.com'
TEST_CLIENT_PASSWORD = '111'
TEST_DESIGNER_EMAIL = 'it@desit.ru'
TEST_DESIGNER_PASSWORD = '111'
