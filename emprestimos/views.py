# biblioteca_web/emprestimos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Emprestimo # Importa o modelo Emprestimo
from .forms import EmprestimoForm # Importa o formulário de Emprestimo
from livros.models import Livro # Importa o modelo Livro
from usuarios.models import CustomUser # Importa o modelo CustomUser, para usar no is_bibliotecario

# Helper para verificar se o usuário é um bibliotecário
def is_bibliotecario(user):
    return user.is_authenticated and user.is_bibliotecario

@login_required
def meus_emprestimos(request):
    # Filtra os empréstimos pelo usuário logado
    emprestimos = Emprestimo.objects.filter(aluno=request.user).order_by('-data_emprestimo')
    
    context = {
        'emprestimos': emprestimos,
        'mensagem': 'Aqui estão seus empréstimos.'
    }
    return render(request, 'emprestimos/meus_emprestimos.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/') # Apenas bibliotecários podem acessar
def realizar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.status = 'emprestado'
            emprestimo.save()
            messages.success(request, f'Empréstimo do livro "{emprestimo.livro.titulo}" para "{emprestimo.aluno.username}" registrado com sucesso!')
            return redirect('emprestimos:meus_emprestimos') # Redireciona para a lista de empréstimos (ou outra página de sucesso)
        else:
            messages.error(request, 'Houve um erro ao registrar o empréstimo. Verifique os dados.')
    else:
        form = EmprestimoForm()
    
    context = {
        'form': form,
        'titulo_pagina': 'Realizar Novo Empréstimo'
    }
    return render(request, 'emprestimos/emprestar_livro.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/') # Apenas bibliotecários podem acessar
def listar_emprestimos_ativos(request):
    # Filtra todos os empréstimos com status 'ativo'
    emprestimos_ativos = Emprestimo.objects.filter(status='emprestado').order_by('data_devolucao_prevista')

    context = {
        'emprestimos_ativos': emprestimos_ativos,
        'titulo_pagina': 'Empréstimos Ativos'
    }
    return render(request, 'emprestimos/emprestimos_ativos.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/')
def devolver_livro(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    # Garante que apenas empréstimos ativos podem ser devolvidos
    if emprestimo.status == 'emprestado':
        emprestimo.marcar_como_devolvido() # Usa o método que você criou no model
        messages.success(request, f'Livro "{emprestimo.livro.titulo}" devolvido com sucesso!')
    else:
        messages.error(request, 'Este empréstimo não está mais ativo.')

    return redirect('emprestimos:listar_emprestimos_ativos') # Redireciona de volta para a lista de ativos