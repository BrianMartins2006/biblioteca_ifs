# biblioteca_web/emprestimos/forms.py

from django import forms
from .models import Emprestimo
from usuarios.models import CustomUser # Precisamos do CustomUser para filtrar alunos
from livros.models import Livro # Precisamos do Livro para filtrar os disponíveis

class EmprestimoForm(forms.ModelForm):
    # Campos personalizados para o formulário
    # O campo 'aluno' será filtrado para mostrar apenas não-bibliotecários
    aluno = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(is_bibliotecario=False),
        label="Aluno"
    )
    # O campo 'livro' será filtrado para mostrar apenas livros disponíveis
    livro = forms.ModelChoiceField(
        queryset=Livro.objects.filter(disponivel=True),
        label="Livro Disponível"
    )

    class Meta:
        model = Emprestimo
        fields = ['livro', 'aluno', 'data_devolucao_prevista']
        widgets = {
            # Adiciona um widget de data e hora para melhor usabilidade no formulário
            'data_devolucao_prevista': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'data_devolucao_prevista': 'Data de Devolução Prevista',
        }

    def clean(self):
        cleaned_data = super().clean()
        livro = cleaned_data.get('livro')
        if livro and not livro.disponivel:
            # Se o livro não estiver disponível (e foi selecionado de alguma forma),
            # adiciona um erro ao formulário.
            self.add_error('livro', 'Este livro não está disponível para empréstimo.')
        return cleaned_data