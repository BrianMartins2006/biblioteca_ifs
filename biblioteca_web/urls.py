# biblioteca_web/urls.py

from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import RedirectView 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', RedirectView.as_view(url='/usuarios/', permanent=False)),

    path('usuarios/', include('usuarios.urls')),
    path('livros/', include('livros.urls')), 
    path('emprestimos/', include('emprestimos.urls')),
]