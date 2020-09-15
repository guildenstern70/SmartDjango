#
#  SmartDjango Python Project
#
#  Copyright (c) 2020 Alessio Saltarin
#  This software is distributed under MIT License.
#  See LICENSE.
#
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'q5oagk40y)-i_+yo%z&8ba47iq!qek&35wu1vef-byk6%3ncns'
DEBUG = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_feather',
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

ROOT_URLCONF = 'SmartDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'SmartDjango.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ibmclouddb',
        'USER': 'ibm_cloud_1e9b93ce_1b3a_4e2b_ada6_dc37a67c86bc',
        'PASSWORD': '09f2f60b2ff00598f325e8c29996222f7a5cdc33d257b468f3277b4ad899e497',
        'HOST': 'd4f3.blrv234f085n1l00bhrg.databases.appdomain.cloud',
        'PORT': '30267',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
            'verbose': {
                'format': '[{levelname} {asctime} {module} {process:d} {thread:d}] {message}',
                'style': '{',
            },
            'simple': {
                'format': '[{levelname} {asctime}] {message}',
                'style': '{',
            },
        },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (
    os.path.join('static'),
)


