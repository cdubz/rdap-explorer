"""
Django settings for rdap_explorer project.
"""

import os
from distutils.util import strtobool

from dotenv import load_dotenv, find_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Environment variables
# Check for and load environment variables from a .env file.

load_dotenv(find_dotenv())

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")
SECRET_KEY = os.environ.get("SECRET_KEY") or None
DEBUG = bool(strtobool(os.environ.get("DEBUG") or "False"))


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'query',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rdap_explorer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rdap_explorer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

config = {
    "ENGINE": os.getenv("DB_ENGINE") or "django.db.backends.sqlite3",
    "NAME": os.getenv("DB_NAME") or os.path.join(BASE_DIR, "data/db.sqlite3"),
}
if os.getenv("DB_USER"):
    config["USER"] = os.getenv("DB_USER")
if os.environ.get("DB_PASSWORD") or os.environ.get("POSTGRES_PASSWORD"):
    config["PASSWORD"] = os.environ.get("DB_PASSWORD") or os.environ.get(
        "POSTGRES_PASSWORD"
    )
if os.getenv("DB_HOST"):
    config["HOST"] = os.getenv("DB_HOST")
if os.getenv("DB_PORT"):
    config["PORT"] = os.getenv("DB_PORT")

DATABASES = {"default": config}


# Cache
# https://docs.djangoproject.com/en/4.0/topics/cache/

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_default",
    }
}


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
