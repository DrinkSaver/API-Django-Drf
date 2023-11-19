import os
from pathlib import Path
from decouple import config, Csv

from datetime import timedelta

# Definition of the basic configuration
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "drf_yasg",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "ApiDrinkSaver",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    "corsheaders",
]

SITE_ID = 1

REST_USE_JWT = True
REST_SESSION_LOGIN = False

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"

# Configuration des templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI Application Configuration
WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.mysql',
        "NAME": config('DB_NAME'),
        "USER": config('DB_USER'),
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST'),
        "PORT": config('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.permissions.IsAuthenticated',
    ]
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Swagger
SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "basic": {
            "type": "basic"
        }
    },
    "USE_SESSION_AUTH": False,
    "JSON_EDITOR": True,
}

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': config('ID_FACEBOOK'),
            'secret': config('SECRET_FACEBOOK')
        },
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'FIELDS': ['email', 'name', 'first_name', 'last_name'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'VERIFIED_EMAIL': True,
    },

    'google': {
        'APP': {
            'client_id': config('ID_GOOGLE'),
            'secret': config('SECRET_GOOGLE'),
        },
        'SCOPE': ['email', 'profile'],
        'AUTH_PARAMS': {'access_type': 'online'},

    },
}

# Email settings for sending outgoing emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')  # L'adresse de votre serveur SMTP
EMAIL_PORT = 587  # Port SMTP (587 est courant pour TLS, utilisez 465 pour SSL)
EMAIL_USE_TLS = True  # Utiliser TLS (si False, utilisez EMAIL_USE_SSL)
EMAIL_USE_SSL = False  # Utiliser SSL (si True, utilisez 465 pour EMAIL_PORT)
EMAIL_HOST_USER = config('EMAIl')  # Votre adresse e-mail d'envoi
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')  # Mot de passe de votre adresse e-mail d'envoi
EMAIL_FROM = config('EMAIl')  # Adresse de l'expéditeur par défaut
DEFAULT_FROM_EMAIL = config('EMAIl')  # Adresse de l'expéditeur par défaut
ACCOUNT_EMAIL_CONFIRMATION_TEMPLATE = 'templates/emails/confirmation_signup_message.txt'
ACCOUNT_PASSWORD_RESET_CONFIRM = 'templates/emails/password_reset_confirmation.txt'

# Setup for password reset with `allauth'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_ADAPTER = "ApiDrinkSaver.adapter.CustomAccountAdapter"

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/account/confirmed-email/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/account/confirmed-email/'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 1800
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
ACCOUNT_EMAIL_MODEL = 'ApiDrinkSaver.CustomEmailAddress'

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USER_MODEL = 'ApiDrinkSaver.CustomUser'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'

ACCOUNT_USERNAME_MIN_LENGTH = 6
ACCOUNT_USERNAME_BLACKLIST = []

ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True

ACCOUNT_SESSION_REMEMBER = None

# CORS (Cross-Origin Resource Sharing) Settings

# List of strings representing URLs allowed to access the API
CORS_ALLOWED_ORIGINS = [
    # "http://127.0.0.1:8000",
    # "http://127.0.0.1:5173",
    # "
]

CORS_ALLOW_ALL_ORIGINS: True

# List of regular patterns representing URLs allowed to access the API.
CORS_ALLOWED_ORIGIN_REGEXES = [
    # r'^https?://\w+\.example\.com$',
]

# Authorization of cookies and identification information
CORS_ALLOW_CREDENTIALS = True

# List of allowed HTTP headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# List of allowed HTTP methods
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
