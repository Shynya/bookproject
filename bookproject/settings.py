from pathlib import Path
import os
#from django.contrib.messages import constants as messages

from datetime import timedelta

from dotenv import load_dotenv
load_dotenv()

#from imagekit.models import ProcessedImageField

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
###SECRET_KEY = 'django-insecure-c3q&8j)&6k(wk1fhncbazix%#7ws@c670s3m&d2jm^cc+ckxxr'
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['chynya.com', 'www.chynya.com', '153.126.191.104','ik1-331-25850.vs.sakura.ne.jp','localhost','127.0.0.1']


# Application definition
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'book.apps.BookConfig',
    'mathfilters',
    #'memo.apps.MemoConfig',
    #'timeline.apps.TimelineConfig',
    #'imagekit',
    #'django.contrib.sites',
   # 'allauth',
   # 'allauth.account',
   # 'allauth.socialaccount',
    #'accounts2.apps.Accounts2Config',
    #'bootstrap4',
    #'photoapp.apps.PhotoappConfig',
    #'rest_framework', #0116追加

    #3rd party apps 0117追加
    #0122非表示　'rest_framework',
    #0122非表示　'djoser',

    # My applications　0117追加
    #'apiv1.apps.Apiv1Config',
    #'shop.apps.ShopConfig',
]

#SITE_ID = 1
#AUTHENTICATION_BACKENDS = (
       # 'allauth.account.auth_backends.AuthenticationBackend',
       # 'django.contrib.auth.backends.ModelBackend',
       # )
#ACCOUNT_AUTHENTICATION_METHOD = 'email'
#ACCOUNT_EMAIL_VERIFICATION = 'none'
#ACCOUNT_USERNAME_REQUIRED = True
#ACCOUNT_EMAIL_REQUIRED = True
#LOGIN_REDIRECT_URL = 'timeline:index'
#ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
#ACCOUNT_LOGOUT_ON_GET = True
#ACCOUNT_EMAIL_SUBJECT_PRRFIX = ''
#ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
#DEFAULT_FROM_EMAIL = 'admin@example.com'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookproject.urls'

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
                'django.template.context_processors.static', #0105追加
            ],
        },
    },
]

STATIC_ROOT = BASE_DIR / 'static'
#STATIC_ROOT = '/var/www/chynya.com/html/djangovenv/bookproject/static'
#STATIC_ROOT = '/usr/share/nginx/html/static'

WSGI_APPLICATION = 'bookproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'database2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database2',
    }
}

DATABASE_ROUTERS = ['book.routers.Router']

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

LANGUAGE_CODE = 'ja'

#0117非表示
#TIME_ZONE = 'UTC'

#0117表示
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

#0117表示
USE_L1ON = True
#0424表示
#USE_L1ON = False

USE_TZ = True
#USE_TZ = False #5/3設定


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'
#MEDIA_ROOT = '/usr/share/nginx/html/media' #0107非表示→表示
#MEDIA_ROOT = '/var/www/chynya.com/html/djangovenv/bookproject/media' #0107追加→0107やっぱり非表示
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'index'

LOGOUT_REDIRECT_URL = 'index'

SIMPLE_JWT = {
        'AUTH_HEADER_TYPES': ('JWT'),
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
}

AUTH_USER_MODEL = 'accounts.CustomUser'

#from django.conf.global_settings import DATETIME_INPUT_FORMATS
#DATETIME_INPUT_FORMATS += ('%Y/%m/%d',) 