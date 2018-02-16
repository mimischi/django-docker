from .common import *  # noqa

INSTALLED_APPS += [
    'django_extensions',
]

# DEBUG
DEBUG = env.bool('DJANGO_DEBUG', default=True)

# SECRET KEY
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='h18i_1j3^d$e6iq8xur&yvbkpk08il9x^&9cf2l2%-0yqx7ss)')

# MAIL
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env(
    'DJANGO_EMAIL_BACKEND',
    default='django.core.mail.backends.console.EmailBackend')

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_app',
        'USER': 'db_user'
        if not env('TRAVIS_CI', default=False) else 'postgres',
        'PASSWORD': 'db_pass',
        'HOST': 'db' if env('PYTHONBUFFERED', default=False) else 'localhost',
        'PORT': 5432,
    }
}

# CACHING
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'werkzeug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

ALLOWED_HOSTS = ['*']
