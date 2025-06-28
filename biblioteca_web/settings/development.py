from .base import *

# Configurações específicas para desenvolvimento
DEBUG = True

ALLOWED_HOSTS = ['*'] # Permite acesso de qualquer host para desenvolvimento

# Database settings for PostgreSQL (from .env)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# SECRET_KEY para desenvolvimento (busca do .env)
SECRET_KEY = os.environ.get('SECRET_KEY')

# Outras configurações de desenvolvimento (ex: logging, debug toolbar)
# INSTALLED_APPS += [
#     'debug_toolbar',
# ]
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]
# INTERNAL_IPS = [
#     '127.0.0.1',
# ]