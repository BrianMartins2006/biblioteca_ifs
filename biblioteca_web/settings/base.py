from pathlib import Path
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Define o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Configurações de segurança (sobrescritas em settings/development.py ou production.py)
SECRET_KEY = os.environ.get('SECRET_KEY') # Obtém a chave do .env
DEBUG = False
ALLOWED_HOSTS = []

# Definição das aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dal',          # Django Autocomplete Light para campos de busca
    'dal_select2',  # Integração do DAL com Select2
    'livros',       # Aplicação de gerenciamento de livros
    'emprestimos',  # Aplicação de empréstimos
    'usuarios',     # Aplicação de usuários
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'biblioteca_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'biblioteca_web', 'templates')],
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

WSGI_APPLICATION = 'biblioteca_web.wsgi.application'

# Configuração de Banco de Dados (sobrescrita em settings/development.py ou production.py)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validação de Senhas
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internacionalização e Localização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Arquivos Estáticos (CSS, JavaScript, Imagens)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Destino para 'collectstatic' em produção

# Arquivos de Mídia (Uploads de usuários)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Modelo de Usuário Customizado
AUTH_USER_MODEL = 'usuarios.CustomUser'