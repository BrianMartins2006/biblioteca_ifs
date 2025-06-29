# biblioteca_web/usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages # Para exibir mensagens
from .forms import CustomUserCreationForm # Importe o formulário de registro

def home(request):
    """
    View para a página inicial do sistema.
    """
    context = {
        'titulo_pagina': 'Página Inicial'
    }
    return render(request, 'usuarios/home.html', context)

def login_view(request):
    """
    View para o login de usuários.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {username}!')
                return redirect('usuarios:home') # Redireciona para a home após o login
            else:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'titulo_pagina': 'Login'
    }
    return render(request, 'usuarios/login.html', context)

def logout_view(request):
    """
    View para o logout de usuários.
    """
    logout(request)
    messages.info(request, 'Você foi desconectado(a).')
    return redirect('usuarios:login') # Redireciona para a página de login após o logout

def registro_view(request):
    """
    View para o registro de novos usuários (alunos).
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Sua conta foi criada com sucesso! Por favor, faça login.')
            return redirect('usuarios:login') # Redireciona para a página de login
        else:
            messages.error(request, 'Houve um erro no registro. Por favor, corrija os erros abaixo.')
    else:
        form = CustomUserCreationForm() # Formulário vazio para GET

    context = {
        'form': form,
        'titulo_pagina': 'Registrar Nova Conta'
    }
    return render(request, 'usuarios/registro.html', context)