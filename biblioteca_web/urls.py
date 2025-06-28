# biblioteca_web/urls.py

from django.contrib import admin
from django.urls import path, include # Importar 'include' para incluir URLs de outros apps
from django.views.generic.base import RedirectView # Para redirecionar a URL raiz

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as URLs de autenticação padrão do Django (login, logout, etc.)
    # O Django fornece views e templates padrões para isso.
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Redireciona a URL raiz para a página inicial (que será em 'usuarios/')
    path('', RedirectView.as_view(url='/usuarios/', permanent=False)),

    # Incluir URLs dos seus apps personalizados
    path('usuarios/', include('usuarios.urls')), # URLs relacionadas a usuários (login, registro, perfil)
    path('livros/', include('livros.urls')),     # URLs relacionadas a livros (busca, detalhes)
    path('emprestimos/', include('emprestimos.urls')), # URLs relacionadas a empréstimos
]
