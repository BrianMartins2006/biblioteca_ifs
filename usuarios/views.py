# biblioteca_web/usuarios/views.py

from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test 


from .forms import CustomUserCreationForm, CustomUserEditForm
from .models import CustomUser 


def is_bibliotecario(user):
    """
    Helper para verificar se o usuário logado é um bibliotecário.
    """
    return user.is_authenticated and user.is_bibliotecario


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
                return redirect('usuarios:home')
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
    return redirect('usuarios:login')

def registro_view(request):
    """
    View para o registro de novos usuários (alunos) pelo público em geral.
    Aqui, is_bibliotecario deve ser sempre False.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.is_bibliotecario = False 
            user.save()
            messages.success(request, 'Sua conta foi criada com sucesso! Por favor, faça login.')
            return redirect('usuarios:login')
        else:
            messages.error(request, 'Houve um erro no registro. Por favor, corrija os erros abaixo.')
    else:
        form = CustomUserCreationForm()
        form.fields.pop('is_bibliotecario_field', None)


    context = {
        'form': form,
        'titulo_pagina': 'Registrar Nova Conta'
    }
    return render(request, 'usuarios/registro.html', context)


@login_required
@user_passes_test(is_bibliotecario, login_url='usuarios:login')
def cadastrar_novo_bibliotecario_ou_aluno(request):
    """
    View para o bibliotecário cadastrar novos usuários (bibliotecários ou alunos)
    pelo frontend.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo usuário cadastrado com sucesso!')
            return redirect('usuarios:lista_usuarios') 
        else:
            messages.error(request, 'Houve um erro ao cadastrar o usuário. Verifique os dados.')
    else:
        form = CustomUserCreationForm() 

    context = {
        'form': form,
        'titulo_pagina': 'Cadastrar Novo Usuário'
    }
    return render(request, 'usuarios/cadastro_usuario_form.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='usuarios:login')
def lista_usuarios(request):
    """
    View para o bibliotecário listar todos os usuários do sistema.
    """
    usuarios = CustomUser.objects.all().order_by('username')
    context = {
        'usuarios': usuarios,
        'titulo_pagina': 'Gerenciar Usuários'
    }
    return render(request, 'usuarios/lista_usuarios.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='usuarios:login')
def editar_usuario(request, pk):
    """
    View para o bibliotecário editar um usuário existente.
    """
    usuario = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuário "{usuario.username}" atualizado com sucesso!')
            return redirect('usuarios:lista_usuarios')
        else:
            messages.error(request, 'Houve um erro ao atualizar o usuário. Verifique os dados.')
    else:
        form = CustomUserEditForm(instance=usuario)

    context = {
        'form': form,
        'usuario': usuario,
        'titulo_pagina': f'Editar Usuário: {usuario.username}'
    }
    return render(request, 'usuarios/editar_usuario_form.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='usuarios:login')
def deletar_usuario(request, pk):
    """
    View para o bibliotecário deletar um usuário.
    """
    usuario = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        if request.user.pk == usuario.pk:
            messages.error(request, 'Você não pode excluir seu próprio usuário!')
            return redirect('usuarios:lista_usuarios')

        usuario.delete()
        messages.success(request, f'Usuário "{usuario.username}" removido com sucesso!')
        return redirect('usuarios:lista_usuarios')

    context = {
        'usuario': usuario,
        'titulo_pagina': 'Confirmar Exclusão de Usuário'
    }
    return render(request, 'usuarios/confirmar_delecao_usuario.html', context)