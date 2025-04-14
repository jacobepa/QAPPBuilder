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
    'METADATA_AUTO_CONF_URL': 'https://wamssoprd.epa.gov/oamfed/idp/metadata',
    # 'METADATA_LOCAL_FILE_PATH': '[The metadata configuration file path]',
    'DEBUG': True,  # Send debug information to a log file
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
        'email': 'mail',
        'username': 'uid',
        'first_name': 'givenname',
        'last_name': 'sn',
    },
    # 'GROUPS_MAP': {  # Optionally allow mapping SAML2 Groups to Django Groups
    #     'SAML Group Name': 'Django Group Name',
    # },
    # 'TRIGGER': {},
    # Custom URL to validate incoming SAML requests against
    'ASSERTION_URL': 'https://qappbuilder.epa.gov',
    # 'ASSERTION_URL': 'https://qappbuilder.epa.gov/sso/acs/',
    # NOTE: The assertion URL is apparently sent as this string above ^
    # with /sso/acs appended. Therefore, when configuring the IDP, the value
    # should be 'https://localhost:8000/sso/acs'...
    # Populates the Issuer element in authn request
    'ENTITY_ID': 'https://qappbuilder.epa.gov/saml2_auth/acs/',
    # 'ENTITY_ID': 'https://localhost:8000/saml2_auth/acs/',
    # Sets the Format property of authn NameIDPolicy element, e.g. 'user.email'
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
                               'qappbuilder.epa.gov'],
    # Accepted time difference between your server and the Identity Provider
    'ACCEPTED_TIME_DIFF': None,
    # Allowed hosts to redirect to using the ?next parameter
    'ALLOWED_REDIRECT_HOSTS': ['localhost', '127.0.0.1',
                               'qappbuilder.epa.gov'],
    # Whether or not to require the token parameter in the SAML assertion
    'TOKEN_REQUIRED': False,
}
