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

USE_SSO_AUTH = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f457efab-86f5-44e4-82e7-be47e4714b04'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'qappbuilder.epa.gov',
                 'v2626umcth964.rtord.epa.gov', '134.67.215.11']

# Application references
INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'accounts',
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: E501
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATETIME_FORMAT = 'N j, Y, P'  # Example: Feb 10, 2025, 5:29 p.m.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'qapp_builder', 'static')

DOWNLOADS_DIR = os.path.join(BASE_DIR, '..', 'docs')

MEDIA_ROOT = os.path.join(BASE_DIR, 'qapp_builder/media')
MEDIA_URL = '/media/'

# We keep upload root separate from STATIC and MEDIA to keep it more secure.
# UPLOAD_ROOT will not be accessible from URL, only by the server views.
UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'uploads')

APP_NAME = 'qapp_builder'
APP_VERSION = '2.0.0'
APP_DISCLAIMER = 'The information and data presented in this product ' + \
                 'were obtained from sources that are believed to be ' + \
                 'reliable. However, in many cases the quality of the ' + \
                 'information or data was not documented by those ' + \
                 'sources; therefore, no claim is made regarding ' + \
                 'their quality.'

LOGGING = {}
SAML2_AUTH = {}

try:
    from .local_settings import *  # noqa: F401
except ImportError:
    pass

# This section contains variables that need to come AFTER local settings are
# taken into consideration. Specifically, SSO AUTH will be required in
# Production environments, but cannot be used in development. Therefore,
# we need to handle it's configuration after we're sure the boolean is True.
if USE_SSO_AUTH:
    INSTALLED_APPS.append('django_saml2_auth')
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
            'saml2.sigver': {
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

    SIGN_REQUESTS = False

    # Auth SAML2
    SAML2_AUTH = {
        # Metadata is required, choose either remote url or local file path
        'METADATA_AUTO_CONF_URL': 'https://wamssostg.epa.gov/oamfed/idp/metadata',  # noqa: E501
        # 'METADATA_LOCAL_FILE_PATH': '[The metadata configuration file path]',

        'DEBUG': True,  # Send debug information to a log file
        # Optional logging configuration.
        # By default, it won't log anything.
        # The following configuration is an example of how to configure the logger,  # noqa: E501
        # which can be used together with the DEBUG option above. Please note that  # noqa: E501
        # the logger config follows the Python's logging configuration schema:
        # https://docs.python.org/3/library/logging.config.html#logging-config-dictschema  # noqa: E501
        'LOGGING': LOGGING,

        # Optional settings below
        # Custom target redirect URL after the user get logged in.
        # Default to /admin if not set. This setting will be overwritten if you
        # have parameter ?next= specificed in the login URL.
        'DEFAULT_NEXT_URL': '/',

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
            # #############################
            'email': 'mail',
            'username': 'uid',
            'first_name': 'givenname',
            'last_name': 'sn',
            # #############################
            # 'mail': 'user.email',
            # 'uid': 'user.username',
            # 'givenname': 'user.first_name',
            # 'sn': 'user.last_name',
            # #############################
            # 'display_name':
            # Mandatory, can be un-required if TOKEN_REQUIRED is False
            # 'token': 'Token',
            # 'groups': 'Groups',  # Optional
            # #############################
        },

        # 'GROUPS_MAP': {  # Optionally allow mapping SAML2 Groups to Django Groups  # noqa: E501
        #     'SAML Group Name': 'Django Group Name',
        # },

        # 'TRIGGER': {},

        # Custom URL to validate incoming SAML requests against
        # 'ASSERTION_URL': 'https://plasticsprojects.epa.gov/saml2_auth/acs/',
        'ASSERTION_URL': 'https://localhost:8000',
        # NOTE: The assertion URL is apparently sent as this string above ^
        # with /sso/acs appended. Therefore, when configuring the IDP, the value
        # should be 'https://localhost:8000/sso/acs'...

        # Populates the Issuer element in authn request
        # 'ENTITY_ID': 'https://plasticsprojects.epa.gov/saml2_auth/acs/',
        'ENTITY_ID': 'https://localhost:8000/saml2_auth/acs/',

        # Sets the Format property of authn NameIDPolicy element, e.g. 'user.email'  # noqa: E501
        'NAME_ID_FORMAT': 'user.email',

        # Set this to True if you are running a Single Page Application (SPA)
        # with Django Rest Framework (DRF), and are using JWT
        # authentication to authorize client users
        'USE_JWT': False,

        # whether of not to get the user in case_sentive mode
        'LOGIN_CASE_SENSITIVE': False,

        # Require each authentication request to be signed
        'AUTHN_REQUESTS_SIGNED': SIGN_REQUESTS,

        # Require each logout request to be signed
        'LOGOUT_REQUESTS_SIGNED': SIGN_REQUESTS,
        # Require each assertion to be signed
        'WANT_ASSERTIONS_SIGNED': SIGN_REQUESTS,
        # Require response to be signed
        'WANT_RESPONSE_SIGNED': SIGN_REQUESTS,

        # Accepted time difference between your server and the Identity Provider
        'ACCEPTED_TIME_DIFF': None,

        # Allowed hosts to redirect to using the ?next parameter
        'ALLOWED_REDIRECT_HOSTS': ['localhost', '127.0.0.1',
                                   'qappbuilder.epa.gov',
                                   'v2626umcth964.rtord.epa.gov'],

        # Whether or not to require the token parameter in the SAML assertion
        'TOKEN_REQUIRED': False,
    }
