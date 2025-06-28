# livros/admin.py

from django.contrib import admin
from .models import Livro

# Registra o modelo Livro no painel de administração do Django.
# Isso permite que os bibliotecários gerenciem livros diretamente pelo /admin.
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista de livros no admin
    list_display = ('titulo', 'autor', 'genero', 'curso_relacionado', 'disponivel', 'ano_publicacao')
    # Campos que podem ser usados para filtrar a lista de livros
    list_filter = ('disponivel', 'genero', 'curso_relacionado', 'ano_publicacao')
    # Campos que podem ser pesquisados
    search_fields = ('titulo', 'autor', 'genero', 'curso_relacionado')
    # Campos que aparecem como links para a página de detalhes do item
    list_display_links = ('titulo',)
    # Campos editáveis diretamente na lista
    list_editable = ('disponivel',)
