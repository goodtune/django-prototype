DEBUG = True
SECRET_KEY = 'a'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    'static',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

INSTALLED_APPS = [
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'prototype.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]
