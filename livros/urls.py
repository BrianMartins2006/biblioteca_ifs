# biblioteca_web/livros/urls.py

from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('deletar/<int:pk>/', views.deletar_livro, name='deletar_livro'),
]