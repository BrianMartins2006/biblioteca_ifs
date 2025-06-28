# emprestimos/admin.py

from django.contrib import admin
from .models import Emprestimo

# Registra o modelo Emprestimo no painel de administração do Django.
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista de empréstimos
    list_display = ('livro', 'aluno', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_real', 'status')
    # Campos para filtrar a lista
    list_filter = ('status', 'data_emprestimo', 'data_devolucao_prevista')
    # Campos para pesquisa
    search_fields = ('livro__titulo', 'aluno__username', 'aluno__matricula') # Permite buscar pelo título do livro e username/matrícula do aluno
    # Campos somente leitura no formulário de edição (data_emprestimo é auto_now_add)
    readonly_fields = ('data_emprestimo',)
    # Configura o autocompletar para ForeignKey para melhorar a usabilidade com muitos livros/alunos
    autocomplete_fields = ('livro', 'aluno')

