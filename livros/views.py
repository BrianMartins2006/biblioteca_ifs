# biblioteca_web/livros/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q 
from django.core.paginator import Paginator

from .models import Livro
from emprestimos.models import Emprestimo 
from usuarios.models import CustomUser 
from .forms import LivroForm 


def is_bibliotecario(user):
    return user.is_authenticated and hasattr(user, 'is_bibliotecario') and user.is_bibliotecario

@login_required
def lista_livros(request):
    """
    Lista todos os livros, com opções de busca e filtro, e com paginação.
    """
    livros_list = Livro.objects.all().order_by('titulo') 
    query = request.GET.get('q')
    genero_filtro = request.GET.get('genero')
    curso_filtro = request.GET.get('curso')

    if query:
        livros_list = livros_list.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query) |
            Q(genero__icontains=query) |
            Q(curso_relacionado__icontains=query)
        )

    if genero_filtro:
        livros_list = livros_list.filter(genero__iexact=genero_filtro)

    if curso_filtro:
        livros_list = livros_list.filter(curso_relacionado__iexact=curso_filtro)

    generos = Livro.objects.order_by('genero').values_list('genero', flat=True).distinct().exclude(genero__isnull=True).exclude(genero__exact='')
    cursos = Livro.objects.order_by('curso_relacionado').values_list('curso_relacionado', flat=True).distinct().exclude(curso_relacionado__isnull=True).exclude(curso_relacionado__exact='')

    livros_por_pagina = 10  
    paginator = Paginator(livros_list, livros_por_pagina)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    
    get_params_copy = request.GET.copy()
    
    if 'page' in get_params_copy:
        get_params_copy.pop('page')
        
    base_query_string = get_params_copy.urlencode()


    context = {
        'page_obj': page_obj, 
        'query': query,
        'genero_filtro': genero_filtro,
        'curso_filtro': curso_filtro,
        'generos': generos,
        'cursos': cursos,
        'base_query_string': base_query_string, 
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