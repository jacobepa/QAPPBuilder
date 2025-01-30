# settings.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# pylint: disable=W0614, W0401

"""
Django settings for qapp_builder project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'REPLACE THIS SECRET KEY IN THE LOCAL SETTINGS. DO NOT COMMIT!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.v2626umcth937.rtord.epa.gov',
                 'https://plasticsprojects.epa.gov/qar5/', '134.67.216.106']

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Auth SAML2
    'django_saml2_auth',
    # Add your apps here to enable them.
    'constants',
    'qapp_builder',
    'support',
    'teams'
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qapp_builder.urls'
APPEND_SLASH = False

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

WSGI_APPLICATION = 'qapp_builder.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'qappbuilder',
        'USER': 'postgres',
        'PASSWORD': 'DEFINE THIS DEFAULT DATABASE IN YOUR LOCAL_SETTINGS.PY',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# Password validation.
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Internationalization.
# https://docs.djangoproject.com/en/2.1/topics/i18n/.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
DATETIME_FORMAT = '%m/%d/%Y %H:%M'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'qapp_builder', 'static')

DOWNLOADS_DIR = os.path.join(BASE_DIR, '..', 'docs')

MEDIA_ROOT = os.path.join(BASE_DIR, 'qapp_builder', 'media')
MEDIA_URL = '/media/'

# We keep upload root separate from STATIC and MEDIA to keep it more secure.
# UPLOAD_ROOT will not be accessible from URL, only by the server views.
UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'uploads')

FILE_UPLOAD_PERMISSIONS = 0o644

ENABLE_RSS_FEEDS = False

APP_NAME = 'qapp_builder'
APP_NAME_LONG = 'QAPP Builder'
APP_VERSION = '2.0.0'
APP_DISCLAIMER = 'The information and data presented in this product ' + \
                 'were obtained from sources that are believed to be ' + \
                 'reliable. However, in many cases the quality of the ' + \
                 'information or data was not documented by those ' + \
                 'sources; therefore, no claim is made regarding ' + \
                 'their quality.'


LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s] %(message)s',  # noqa: E501
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'level': 'DEBUG',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'saml2': {
            'level': 'DEBUG'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': [
            'stdout',
        ],
    },
}

# Auth SAML2
SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    'METADATA_AUTO_CONF_URL': '[The auto(dynamic) metadata conf URL of SAML2]',
    'METADATA_LOCAL_FILE_PATH': '[The metadata configuration file path]',
    'KEY_FILE': '[The key file path]',
    'CERT_FILE': '[The certificate file path]',

    'DEBUG': False,  # Send debug information to a log file
    # Optional logging configuration.
    # By default, it won't log anything.
    # The following configuration is an example of how to configure the logger,
    # which can be used together with the DEBUG option above. Please note that
    # the logger config follows the Python's logging configuration schema:
    # https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
    'LOGGING': LOGGING,

    # Optional settings below
    # Custom target redirect URL after the user get logged in.
    # Default to /admin if not set. This setting will be overwritten if you
    # have parameter ?next= specificed in the login URL.
    'DEFAULT_NEXT_URL': '/admin',

    # Create a new Django user when a new user logs in. Defaults to True.
    'CREATE_USER': True,
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': False,  # The staff status for new users
        'SUPERUSER_STATUS': False,  # The superuser status for new users
    },
    # Change Email/UserName/FirstName/LastName to corresponding SAML2
    # userprofile attributes.
    'ATTRIBUTES_MAP': {
        'email': 'user.email',
        'username': 'user.username',
        'first_name': 'user.first_name',
        'last_name': 'user.last_name',
        # Mandatory, can be un-required if TOKEN_REQUIRED is False
        'token': 'Token',
        'groups': 'Groups',  # Optional
    },
    'GROUPS_MAP': {  # Optionally allow mapping SAML2 Groups to Django Groups
        'SAML Group Name': 'Django Group Name',
    },
    'TRIGGER': {
        # Optional: needs to return a User Model instance or None
        # 'GET_USER': 'path.to.your.get.user.hook.method',

        # 'CREATE_USER': 'path.to.your.new.user.hook.method',
        # 'BEFORE_LOGIN': 'path.to.your.login.hook.method',
        # 'AFTER_LOGIN': 'path.to.your.after.login.hook.method',

        # Optional. This is executed right before METADATA_AUTO_CONF_URL.
        # For systems with many metadata files registered allows to
        # narrow the search scope.
        # 'GET_USER_ID_FROM_SAML_RESPONSE': 'path.to.your.get.user.from.saml.hook.method',  # noqa: E501

        # This can override the METADATA_AUTO_CONF_URL to enumerate
        # all existing metadata autoconf URLs
        # 'GET_METADATA_AUTO_CONF_URLS': 'path.to.your.get.metadata.conf.hook.method',  # noqa: E501
    },
    # Custom URL to validate incoming SAML requests against
    'ASSERTION_URL': 'https://mysite.com',

    # Populates the Issuer element in authn request
    'ENTITY_ID': 'https://mysite.com/saml2_auth/acs/',

    # Sets the Format property of authn NameIDPolicy element, e.g. 'user.email'
    'NAME_ID_FORMAT': 'user.email',

    # Set this to True if you are running a Single Page Application (SPA)
    # with Django Rest Framework (DRF), and are using JWT
    # authentication to authorize client users
    'USE_JWT': False,

    # 'JWT_ALGORITHM': 'HS256',  # JWT algorithm to sign the message with
    # 'JWT_SECRET': 'your.jwt.secret',  # JWT secret to sign the message with

    # # Private key to sign the message with.
    # # The algorithm should be set to RSA256 or a more secure alternative.
    # 'JWT_PRIVATE_KEY': '--- YOUR PRIVATE KEY ---',

    # # If your private key is encrypted, you might need to provide
    # # a passphrase for decryption
    # 'JWT_PRIVATE_KEY_PASSPHRASE': 'your.passphrase',

    # # Public key to decode the signed JWT token
    # 'JWT_PUBLIC_KEY': '--- YOUR PUBLIC KEY ---',

    # 'JWT_EXP': 60,  # JWT expiry time in seconds

    # # Redirect URL for the client if you are using JWT auth with DRF.
    # # See explanation below
    # 'FRONTEND_URL': 'https://myfrontendclient.com',

    # whether of not to get the user in case_sentive mode
    'LOGIN_CASE_SENSITIVE': False,

    # Require each authentication request to be signed
    'AUTHN_REQUESTS_SIGNED': True,

    'LOGOUT_REQUESTS_SIGNED': True,  # Require each logout request to be signed
    'WANT_ASSERTIONS_SIGNED': True,  # Require each assertion to be signed
    'WANT_RESPONSE_SIGNED': True,  # Require response to be signed

    # Accepted time difference between your server and the Identity Provider
    'ACCEPTED_TIME_DIFF': None,

    # Allowed hosts to redirect to using the ?next parameter
    'ALLOWED_REDIRECT_HOSTS': ['localhost', '127.0.0.1',
                                'qappbuilder.epa.gov'],

    # Whether or not to require the token parameter in the SAML assertion
    'TOKEN_REQUIRED': True,
}

try:
    from .local_settings import *
    # py-lint: disable=E0012
except ImportError:
    pass
