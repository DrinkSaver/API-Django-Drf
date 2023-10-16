import os
from pathlib import Path
from decouple import config, Csv
from datetime import timedelta
from config import certificates

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_jwt",
    "ApiDrinkSaver",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.mysql',
        "NAME": config('DB_NAME'),
        "USER": config('DB_USER'),
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST'),
        "PORT": config('DB_PORT'),
        "TEST": {
            'NAME': 'myproject_test',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {
        "basic": {
            "type": "basic"
        }
    },
    "PERSIST_AUTH": True,
}

# Utilisation de JSON Web Token pour l'authentification
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Configurations spécifiques à djangorestframework simplejwt
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=7),
    'SLIDING_TOKEN_LIFETIME_REFRESH_LIFETIME': timedelta(days=14),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=14),
}

# Paramètres de messagerie pour l'envoi d'e-mails sortants
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Backend d'e-mail SMTP
EMAIL_HOST = 'smtp.gmail.com'  # L'adresse de votre serveur SMTP
EMAIL_PORT = 587  # Port SMTP (587 est courant pour TLS, utilisez 465 pour SSL)
EMAIL_USE_TLS = True  # Utiliser TLS (si False, utilisez EMAIL_USE_SSL)
EMAIL_USE_SSL = False  # Utiliser SSL (si True, utilisez 465 pour EMAIL_PORT)
EMAIL_SSL_CAFILE = False #os.path.join(BASE_DIR, 'ApiDrinkSaver.config.certificates', 'cacert.pem')
EMAIL_HOST_USER = 'zychsteeve4@gmail.com'  # Votre adresse e-mail d'envoi
EMAIL_HOST_PASSWORD = 'ldytzdhmvunjbvoo'  # Mot de passe de votre adresse e-mail d'envoi
EMAIL_FROM = 'zychsteeve4@gmail.com'  # Adresse de l'expéditeur par défaut
DEFAULT_FROM_EMAIL = 'zychsteeve4@gmail.com'  # Adresse de l'expéditeur par défaut
