"""
Django settings for this project.
Generated by 'django-admin startproject' using Django 2.2.11.
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

DEBUG_PROPAGATE_EXCEPTIONS = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leaflet',
    'django.contrib.gis',
    'core',
    'org',
    'widget_tweaks',
    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'simple_history',
    'pipeline',
    'admin_honeypot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    'default': env.db(),
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),

)

LANGUAGE_CODE = 'id'

TIME_ZONE = 'America/Asuncion'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT= os.path.join(BASE_DIR, 'allstatic')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_URL = '/static/'

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'


LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-25.292, -57.551),
    'DEFAULT_ZOOM': 11,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'RESET_VIEW': False,
    'NO_GLOBALS': False,

    'PLUGINS': {
        'markercluster': {
            'css': 'https://leaflet.github.io/Leaflet.markercluster/dist/MarkerCluster.Default.css',
            'js': 'https://leaflet.github.io/Leaflet.markercluster/dist/leaflet.markercluster-src.js',
            'auto-include': True,
        },
        'fullscreen': {
            'css': 'https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/leaflet.fullscreen.css',
            'js': 'https://api.mapbox.com/mapbox.js/plugins/leaflet-fullscreen/v1.0.1/Leaflet.fullscreen.min.js',
            'auto-include': True,
        },
    }
}


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 25,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        #'rest_framework.renderers.BrowsableAPIRenderer',  # Uncomment this like if you want to use the nice API view for dev
    )
}

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# Configs related to django-pipeline
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder'
)
PIPELINE = {
    'PIPELINE_ENABLED': True,
    'PIPELINE_COLLECTOR_ENABLED': True,
    'JAVASCRIPT': {
        'table-view.js': {
                'source_filenames': (
                    'scripts/table-view.js',
                ),
                'output_filename': 'scripts/table-view.min.js',
        },
        'list.js': {
                'source_filenames': (
                    'scripts/list.js',
                ),
                'output_filename': 'scripts/list.min.js',
        },
        'list-donation.js': {
                'source_filenames': (
                    'scripts/list-donation.js',
                ),
                'output_filename': 'scripts/list-donation.min.js',
        },
        'leaflet-patch.js': {
                'source_filenames': (
                    'scripts/leaflet-patch.js',
                ),
                'output_filename': 'scripts/leaflet-patch.min.js',
        },
        'requests-linechart.js': {
                'source_filenames': (
                    'scripts/requests-linechart.js',
                ),
                'output_filename': 'scripts/requests-linechart.min.js',
        },
        'libs/apexcharts.js': {
                'source_filenames': (
                    'libs/apexcharts.js',
                ),
                'output_filename': 'libs/apexcharts.min.js',
        },
        'libs/bulma-calendar/bulma-calendar.js': {
                'source_filenames': (
                    'libs/bulma-calendar/bulma-calendar.js',
                ),
                'output_filename': 'libs/bulma-calendar/bulma-calendar.min.js',
        }
    },
    'STYLESHEETS': {
        'libs/bulma-calendar/bulma-calendar.css': {
            'source_filenames': (
                'libs/bulma-calendar/bulma-calendar.min.css',
            ),
            'output_filename': 'libs/bulma-calendar/bulma-calendar.min.css',
        }
    },
    'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor'
}

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
