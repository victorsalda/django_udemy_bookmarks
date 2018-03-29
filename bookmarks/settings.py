"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g9ev0c-6bfk-!oiqj#h)1xbp=7%c)io5!%daqf#w$3x^*$@#h4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth', # here is include the authentication framework.
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'bookmarks.urls'

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

WSGI_APPLICATION = 'bookmarks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = { # Dictionary with all the data bases for the project.

              # Django needs to store all it does (users, tables, apps, etc.) in a data base.
              # Django support: PostgreSQL, MySQL, SQLite and Oracle.

              # There are three MySQL libraries (clients in servers world) for Python that are currently maintained:
              # 1. mysqlclient - By far the fastest MySQL connector for CPython. Requires the mysql-connector-c C library to work.
              # 2. PyMySQL - Pure Python MySQL client. According to the maintainer of both mysqlclient and MyPySQL, you should use PyMySQL if:
                    # You can't use libmysqlclient for some reason.
                    # You want to use monkeypatched socket of gevent or eventlet.
                    # You wan't to hack mysql protocol.
              # 3. mysql-connector-python - MySQL connector developed by the MySQL group at Oracle, also written entirely in Python.
                    # It's performance appears to be the worst out of the three. Also, due to some licensing issues, you can't download it from PyPI (but it's now available through conda).

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'victor_django_bookmarks',
        'USER': 'root',
        'PASSWORD': '9PAv32ekC4ioziyg',
        'HOST': '35.187.28.136',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

# configuration of the SMTP server to send email. In this case using the google one.

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'victor@verticaldataanalytics.com'

EMAIL_HOST_PASSWORD = 'vicsal20'

EMAIL_PORT = 587

EMAIL_USE_TLS = True


# if you don't want to send email using a SMTP server you cn use the django built-in function.

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# setting the haystack. Haystack provides modular search for Django.
# It features a unified, familiar API that allows you to plug in
# different search backends (such as Solr, Elasticsearch, Whoosh,
# Xapian, etc.) without having to modify your code.

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/blog'
    },
}

