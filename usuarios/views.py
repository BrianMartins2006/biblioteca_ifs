# biblioteca_web/usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm # Formulário de autenticação padrão do Django
from django.contrib import messages # Para exibir mensagens
from .forms import CustomUserCreationForm 

def home(request):
    # Esta será a página inicial.
    # Pode exibir informações diferentes dependendo se o usuário está logado ou não.
    return render(request, 'usuarios/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redireciona para a página 'home' após o login bem-sucedido
                return redirect('usuarios:home')
            else:
                # Mensagem de erro se a autenticação falhar
                form.add_error(None, "Nome de usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('usuarios:home') # Redireciona para a página inicial após o logout

def registro_view(request):
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