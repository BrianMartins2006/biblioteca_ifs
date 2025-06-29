# biblioteca_web/emprestimos/admin.py

from django.contrib import admin
from .models import Emprestimo # Importa o seu modelo Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'aluno', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_real', 'status')
    list_filter = ('status', 'data_emprestimo', 'data_devolucao_prevista')
    search_fields = ('livro__titulo', 'aluno__username', 'aluno__first_name', 'aluno__last_name') # Permite buscar pelo título do livro ou nome/usuário do aluno
    raw_id_fields = ('livro', 'aluno') # Melhora a usabilidade ao selecionar livro/aluno no admin