# biblioteca_web/emprestimos/admin.py

from django.contrib import admin
from .models import Emprestimo 

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'aluno', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_real', 'status')
    list_filter = ('status', 'data_emprestimo', 'data_devolucao_prevista')
    search_fields = ('livro__titulo', 'aluno__username', 'aluno__first_name', 'aluno__last_name') 
    raw_id_fields = ('livro', 'aluno') 