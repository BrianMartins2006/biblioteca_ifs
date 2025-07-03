# biblioteca_web/usuarios/urls.py (modifique o arquivo existente)

from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('cadastrar/', views.cadastrar_novo_bibliotecario_ou_aluno, name='cadastrar_novo_usuario'),
    path('lista/', views.lista_usuarios, name='lista_usuarios'),          
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'), 
    path('deletar/<int:pk>/', views.deletar_usuario, name='deletar_usuario'), 
]