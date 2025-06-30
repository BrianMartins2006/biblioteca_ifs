# biblioteca_web/emprestimos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import Emprestimo
from livros.models import Livro
from usuarios.models import CustomUser
from .forms import EmprestimoForm
from dal import autocomplete


def is_bibliotecario(user):
    return user.is_authenticated and user.is_bibliotecario

class LivroAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Livro.objects.none()

        qs = Livro.objects.all()

        if self.q:
            qs = qs.filter(titulo__icontains=self.q) 
        
        qs = qs.filter(disponivel=True)

        return qs

class AlunoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return CustomUser.objects.none()

        qs = CustomUser.objects.all()

        if self.q:
            qs = qs.filter(username__icontains=self.q) | \
                 qs.filter(first_name__icontains=self.q) | \
                 qs.filter(last_name__icontains=self.q)
        
        qs = qs.filter(is_bibliotecario=False)

        return qs



@login_required
def meus_emprestimos(request):
    """
    Lista os empréstimos do usuário logado.
    """
    emprestimos = Emprestimo.objects.filter(aluno=request.user).order_by('-data_emprestimo')
    
    context = {
        'emprestimos': emprestimos,
        'titulo_pagina': 'Meus Empréstimos'
    }
    return render(request, 'emprestimos/meus_emprestimos.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/')
def realizar_emprestimo(request):
    """
    Permite ao bibliotecário realizar um novo empréstimo.
    """
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            
            livro = emprestimo.livro
            if not livro.disponivel:
                messages.error(request, f'O livro "{livro.titulo}" não está disponível para empréstimo.')
            else:
                emprestimo.save()
                livro.disponivel = False
                livro.save()
                messages.success(request, f'Empréstimo do livro "{livro.titulo}" para "{emprestimo.aluno.username}" realizado com sucesso!')
                return redirect('emprestimos:listar_emprestimos_ativos')
        else:
            messages.error(request, 'Houve um erro ao realizar o empréstimo. Verifique os dados.')
    else:
        form = EmprestimoForm()
    
    context = {
        'form': form,
        'titulo_pagina': 'Realizar Novo Empréstimo'
    }
    return render(request, 'emprestimos/emprestar_livro.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/')
def devolver_emprestimo(request, emprestimo_id):
    """
    Permite ao bibliotecário registrar a devolução de um livro.
    """
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    if request.method == 'POST':
        if emprestimo.data_devolucao_real is None:
            emprestimo.marcar_como_devolvido()
            messages.success(request, f'Livro "{emprestimo.livro.titulo}" devolvido com sucesso por "{emprestimo.aluno.username}".')
        else:
            messages.info(request, f'O empréstimo do livro "{emprestimo.livro.titulo}" já havia sido devolvido.')
        return redirect('emprestimos:listar_emprestimos_ativos')
    
    context = {
        'emprestimo': emprestimo,
        'titulo_pagina': 'Confirmar Devolução'
    }
    return render(request, 'emprestimos/confirmar_devolucao.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/')
def listar_emprestimos_ativos(request):
    """
    Lista todos os empréstimos ativos (não devolvidos) para bibliotecários.
    """
    emprestimos_ativos = Emprestimo.objects.filter(data_devolucao_real__isnull=True).order_by('data_devolucao_prevista')
    
    context = {
        'emprestimos_ativos': emprestimos_ativos,
        'titulo_pagina': 'Empréstimos Ativos'
    }
    return render(request, 'emprestimos/emprestimos_ativos.html', context)

@login_required
@user_passes_test(is_bibliotecario, login_url='/usuarios/login/')
def listar_emprestimos_atrasados(request):
    emprestimos_atrasados_query = Emprestimo.objects.filter(
        data_devolucao_real__isnull=True,
        data_devolucao_prevista__lt=timezone.now()
    ).order_by('data_devolucao_prevista')

    emprestimos_com_atraso_calculado = []
    for emprestimo in emprestimos_atrasados_query:
        diferenca = timezone.now() - emprestimo.data_devolucao_prevista
        emprestimo.dias_atraso = diferenca.days
        emprestimos_com_atraso_calculado.append(emprestimo)

    context = {
        'emprestimos_atrasados': emprestimos_com_atraso_calculado,
        'titulo_pagina': 'Livros em Atraso',
    }
    return render(request, 'emprestimos/emprestimos_atrasados.html', context)