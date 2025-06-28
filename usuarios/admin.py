# usuarios/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Registra o modelo CustomUser no painel de administração do Django.
# Usamos UserAdmin para manter a funcionalidade padrão do admin de usuários e adicionar nossos campos.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Adiciona os campos 'is_bibliotecario' e 'matricula' aos fieldsets do admin.
    # Isso os torna visíveis e editáveis no formulário de detalhes do usuário.
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_bibliotecario', 'matricula')}),
    )
    # Adiciona 'is_bibliotecario' e 'matricula' à lista de exibição no admin
    list_display = UserAdmin.list_display + ('is_bibliotecario', 'matricula')
    # Adiciona 'is_bibliotecario' ao filtro da lista
    list_filter = UserAdmin.list_filter + ('is_bibliotecario',)
    # Adiciona 'matricula' aos campos de busca
    search_fields = UserAdmin.search_fields + ('matricula',)

