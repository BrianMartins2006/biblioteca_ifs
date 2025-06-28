import os

# Define qual ambiente de settings será carregado
# A variável de ambiente DJANGO_SETTINGS_MODULE é definida no docker-compose.yml
# Ex: DJANGO_SETTINGS_MODULE=biblioteca_web.settings.development
# Isso permite que você mude as configurações sem modificar o código diretamente.
settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')

if settings_module:
    # Carrega as configurações dinamicamente
    # Por exemplo, se DJANGO_SETTINGS_MODULE for 'biblioteca_web.settings.development',
    # ele importará o módulo 'development' dentro do pacote 'settings'.
    try:
        module = __import__(settings_module, fromlist=['*'])
        for key in dir(module):
            if not key.startswith('__'):
                globals()[key] = getattr(module, key)
    except ImportError:
        # Fallback para base.py se a variável de ambiente não for válida
        print(f"Aviso: Não foi possível carregar as configurações de '{settings_module}'. Carregando 'base.py' como fallback.")
        from .base import *
else:
    # Se DJANGO_SETTINGS_MODULE não estiver definido, usa base.py
    print("Aviso: Variável de ambiente 'DJANGO_SETTINGS_MODULE' não definida. Carregando 'base.py'.")
    from .base import *