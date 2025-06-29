# biblioteca_web/livros/admin.py

from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'curso_relacionado', 'disponivel', 'ano_publicacao')
    list_filter = ('disponivel', 'genero', 'curso_relacionado', 'ano_publicacao')
    search_fields = ('titulo', 'autor', 'genero', 'curso_relacionado')
    list_display_links = ('titulo',)
    list_editable = ('disponivel',)