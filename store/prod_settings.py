from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure--7r307faskl;jfasilftf(fcc1qj)lk69w*k)!mph9)i_i$-'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'website',
        'USER': 'mark',
        'PASSWORD': 'sUperITshn(1)k',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
