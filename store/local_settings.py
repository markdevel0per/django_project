from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure--7r3074wbjj0kfydml3(9tf(fcc1qj)lk69w*k)!mph9)i_i$-'

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'website',
        'USER': 'mark',
        'PASSWORD': 'sUperITshn(1)k',
    }
}
