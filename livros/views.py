# biblioteca_web/livros/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q # Para consultas complexas
# from django.utils import timezone # Não é mais necessário aqui, foi movido para emprestimos/views.py

from .models import Livro
from .forms import LivroForm

# Helper para verificar se o usuário é um bibliotecário
def is_bibliotecario(user):
    return user.is_authenticated and user.is_bibliotecario

@login_required
def lista_livros(request):
    """
    Lista todos os livros, com opções de busca e filtro.
    """
    livros = Livro.objects.all()
    query = request.GET.get('q')
    genero_filtro = request.GET.get('genero')
    curso_filtro = request.GET.get('curso')

    if query:
        livros = livros.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(genero__icontains=query) |
            Q(curso_relacionado__icontains=query)
        )

    if genero_filtro:
        livros = livros.filter(genero__iexact=genero_filtro)

    if curso_filtro:
        livros = livros.filter(curso_relacionado__iexact=curso_filtro)

    # Obter gêneros e cursos únicos para os filtros
    generos = Livro.objects.order_by('genero').values_list('genero', flat=True).distinct().exclude(genero__isnull=True).exclude(genero__exact='')
    cursos = Livro.objects.order_by('curso_relacionado').values_list('curso_relacionado', flat=True).distinct().exclude(curso_relacionado__isnull=True).exclude(curso_relacionado__exact='')

    context = {
        'livros': livros,
        'query': query,
        'genero_filtro': genero_filtro,
        'curso_filtro': curso_filtro,
        'generos': generos,
        'cursos': cursos,
        'titulo_pagina': 'Lista de Livros'
    }
    return render(request, 'livros/lista_livros.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/')
def cadastrar_livro(request):
    """
    Permite ao bibliotecário cadastrar um novo livro.
    """
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('livros:lista_livros')
        else:
            messages.error(request, 'Houve um erro ao cadastrar o livro. Verifique os dados.')
    else:
        form = LivroForm()
    
    context = {
        'form': form,
        'titulo_pagina': 'Cadastrar Novo Livro'
    }
    return render(request, 'livros/livro_form.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/')
def editar_livro(request, pk):
    """
    Permite ao bibliotecário editar um livro existente.
    """
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('livros:lista_livros')
        else:
            messages.error(request, 'Houve um erro ao atualizar o livro. Verifique os dados.')
    else:
        form = LivroForm(instance=livro)
    
    context = {
        'form': form,
        'titulo_pagina': 'Editar Livro'
    }
    return render(request, 'livros/livro_form.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/')
def deletar_livro(request, pk):
    """
    Permite ao bibliotecário deletar um livro existente.
    """
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro removido com sucesso!')
        return redirect('livros:lista_livros')
    context = {
        'livro': livro,
        'titulo_pagina': 'Confirmar Exclusão de Livro'
    }
    return render(request, 'livros/confirmar_delecao_livro.html', context)