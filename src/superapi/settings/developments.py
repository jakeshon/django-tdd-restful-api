from .base import *

PROJECT_APPS = [
        'posts',
]

OPTIONAL_APPS = [
        'django_extensions',
]

INSTALLED_APPS = PREQ_APPS + PROJECT_APPS + OPTIONAL_APPS

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
