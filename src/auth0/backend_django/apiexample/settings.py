import os
from drypy.django import auth0_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a819@)zd0&536k68f%n3)t1+t(d@-44ehevjps-2)#@k7bsjc^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'apiexample.urls'

WSGI_APPLICATION = 'apiexample.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = auth0_settings.INSTALLED_APPS
MIDDLEWARE = auth0_settings.MIDDLEWARE
CORS_ORIGIN_ALLOW_ALL = auth0_settings.CORS_ORIGIN_ALLOW_ALL
REST_FRAMEWORK = auth0_settings.REST_FRAMEWORK
JWT_AUTH = auth0_settings.jwt_auth('dry-play.auth0.com', 'https://dry-play-api1.com')
