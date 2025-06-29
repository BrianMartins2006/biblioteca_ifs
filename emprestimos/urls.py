# biblioteca_web/emprestimos/urls.py (continue adicionando ao arquivo existente)

from django.urls import path
from . import views

app_name = 'emprestimos'

urlpatterns = [
    path('meus/', views.meus_emprestimos, name='meus_emprestimos'),
    path('emprestar/', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('ativos/', views.listar_emprestimos_ativos, name='listar_emprestimos_ativos'), # <-- Adicione esta linha
    path('devolver/<int:emprestimo_id>/', views.devolver_livro, name='devolver_livro'), # <-- Adicione esta linha
    # Suas outras URLs para empréstimos virão aqui no futuro
]