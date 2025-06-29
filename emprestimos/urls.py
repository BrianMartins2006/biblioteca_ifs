# biblioteca_web/emprestimos/urls.py

from django.urls import path
from . import views

app_name = 'emprestimos'

urlpatterns = [
    path('meus/', views.meus_emprestimos, name='meus_emprestimos'),
    path('emprestar/', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('ativos/', views.listar_emprestimos_ativos, name='listar_emprestimos_ativos'),
    path('devolver/<int:emprestimo_id>/', views.devolver_emprestimo, name='devolver_emprestimo'), # <-- CORREÇÃO AQUI
    path('atrasados/', views.listar_emprestimos_atrasados, name='listar_emprestimos_atrasados'), # <-- CONFIRME SE ESTA LINHA ESTÁ PRESENTE TAMBÉM
    # Suas outras URLs para empréstimos virão aqui no futuro
]