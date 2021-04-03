import os
import json
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', "secret_key")

DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(',')


INSTALLED_APPS = [
    'todo_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.vk',
    'tasks.apps.TasksConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ToDo.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'ToDo.wsgi.application'

if os.getenv('ENVIRONMENT', 'local') == 'local':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.{}'.format(
                os.getenv('DATABASE_ENGINE', 'sqlite3')
            ),
            'NAME': os.getenv('DATABASE_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
            'USER': os.getenv('DATABASE_USERNAME', 'todo'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD', 'password'),
            'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
            'PORT': os.getenv('DATABASE_PORT', 3306),
            'OPTIONS': json.loads(
                os.getenv('DATABASE_OPTIONS', '{}')
            ),
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_ROOT = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), os.pardir)

if os.getenv('ENVIRONMENT', 'local') == 'local':
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    UPLOAD_ROOT = 'uploads/'

    DOWNLOAD_URL = STATIC_URL + "media/downloads"
    DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
# for prod environment
else:

    DEFAULT_FILE_STORAGE = 'ToDo.gcloud.GoogleCloudMediaFileStorage'
    STATICFILES_STORAGE = 'ToDo.gcloud.GoogleCloudStaticFileStorage'

    GS_PROJECT_ID = os.getenv('PROJECT_ID')
    GS_STATIC_BUCKET_NAME = os.getenv('BUCKET')
    # same as STATIC BUCKET if using single bucket both for static and media
    GS_MEDIA_BUCKET_NAME = os.getenv('BUCKET')

    STATIC_URL = 'https://storage.googleapis.com/{}/'.format(
        GS_STATIC_BUCKET_NAME)
    STATIC_ROOT = "static/"

    MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(
        GS_MEDIA_BUCKET_NAME)
    MEDIA_ROOT = "media/"

    UPLOAD_ROOT = 'media/uploads/'

    DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
    DOWNLOAD_URL = STATIC_URL + "media/downloads"

LOGOUT_REDIRECT_URL = 'index'

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
