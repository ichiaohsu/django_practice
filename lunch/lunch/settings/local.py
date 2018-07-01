from .base import *

SECRET_KEY = 'bWFuYWdlLnB55Yiw5bqV5piv5bm55Zib55qECg=='
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}