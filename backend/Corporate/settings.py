import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'rvf6%iy!+q87u5owk&3#=#y7ek+9dsygapz^+0+^rhre)nr@p+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'base.apps.BaseConfig',
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

ROOT_URLCONF = 'Corporate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.context_processors.footerdata',  # footer data
                'base.context_processors.news',  # Newsletters Form
                'base.context_processors.headerdata',  # Header Data
            ],
        },
    },
]

WSGI_APPLICATION = 'Corporate.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (BASE_DIR / 'locale',)

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    BASE_DIR / 'base/static',
    BASE_DIR / 'static',
)
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = 'staticfiles/static'

AUTH_USER_MODEL = 'accounts.User'

# Logs
LOG_DIR = BASE_DIR / 'logs'
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOGGING = {'version': 1,
           'disable_existing_loggers': False,
           'formatters': {
               'console': {
                   'format': '%(name)-12s %(levelname)-8s %(message)s'
               },
               'file': {
                   'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
               }
           },
           'handlers': {
               'console': {
                   'class': 'logging.StreamHandler',
                   'formatter': 'console'
               },
               'file': {
                   'level': 'DEBUG',
                   'class': 'logging.FileHandler',
                   'formatter': 'file',
                   'filename': BASE_DIR / 'logs/Corporate.log'
               }
           },
           'loggers': {
               '': {
                   'level': 'DEBUG',
                   'handlers': ['console', 'file']
               }
           },
           'celery': {
               'handlers': ['console'],
               'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
           },
           }

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
    "https://business.sjpy.ir/",
]
