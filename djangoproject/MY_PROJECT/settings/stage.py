from PROJECT_NAME.settings.base import *
import environ

env = environ.Env(DEBUG=(bool, False),)

CURRENT_ENV = 'stage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/django/frontend/'],
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

TEMPLATE_DIRS = ('/home/django/frontend/',)
