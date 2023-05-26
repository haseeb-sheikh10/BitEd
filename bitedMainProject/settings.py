"""
Django settings for bitedMainProject project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# See https://realpython.com/django-nginx-gunicorn/

# SECURITY WARNING: keep the secret key used in production secret!
try: 
    SECRET_KEY = os.environ["SECRET_KEY"]
except KeyError:
    SECRET_KEY = None
if SECRET_KEY is None:
    SECRET_KEY = os.getenv('SECRET_KEY')
if SECRET_KEY is  None:
    SECRET_KEY = env('SECRET_KEY')
if SECRET_KEY is None:
    SECRET_KEY = 'django-insecure-_+b48@r2t#ttge5s9(08j^rikbh!*xto$4)a9=^l&7@=q=4_*q'
# SECURITY WARNING: don't run with debug turned on in production!
try: 
    DEBUG = os.environ["DEBUG"]
except KeyError:
    DEBUG = None
if SECRET_KEY is None:
    DEBUG = os.getenv('DEBUG')
if DEBUG is None:
    DEBUG = env('DEBUG')
if  DEBUG is None:
    DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'verify_email.apps.VerifyEmailConfig',
    'bitedMainProject',
    'crispy_bootstrap5',
    'social_django',
    'registration',
    'crispy_forms',
    'questions',
    'profile',
    'writing',
    'taggit',
    'tiles',
    'home',
    'map',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'bitedMainProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'bitedMainProject.wsgi.application'

DEFAULT_DOMAIN = 'http://tvildiani.com'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ["DBENGINE"],
        'NAME': os.environ["DBNAME"],
        'USER': os.environ["DBUSER"],
        'PASSWORD': os.environ["DBPASSWORD"],
        'HOST': os.environ["DBHOST"],
        'PORT': os.environ["PORT"],
    }

#   'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
    
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = '/var/www/static/'

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

# extra places to find static filed outside static folder inside installed apps
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL= '/'
LOGOUT_REDIRECT_URL = '/'

# Emailing settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_FROM = env('EMAIL_FROM')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('GMAILAPPPASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 14400

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# Social Login Configuration

try:
    from bitedMainProject import facebook_settings
    SOCIAL_AUTH_FACEBOOK_KEY = facebook_settings.SOCIAL_AUTH_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET = facebook_settings.SOCIAL_AUTH_FACEBOOK_SECRET
except:
    print('NO SOCIAL LOGIN CONFIGURED')

SOCIAL_AUTH_JSONFIELD_ENABLED = True

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

# SOCIAL_AUTH_URL_NAMESPACE = 'registration'


# Caching 
# add(), set(), touch() cull cache only
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "Bited_main_cache_table",
    }
}
