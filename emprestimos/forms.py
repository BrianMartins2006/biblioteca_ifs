# biblioteca_web/emprestimos/forms.py

from django import forms
from .models import Emprestimo
from livros.models import Livro
from usuarios.models import CustomUser
import dal.autocomplete 

class EmprestimoForm(forms.ModelForm):
    # Não é necessário definir 'aluno' e 'livro' como ModelChoiceField aqui,
    # pois o widget dal.autocomplete.ModelSelect2 cuida da seleção e da busca.
    # Os filtros serão feitos nas views de autocomplete (LivroAutocomplete, AlunoAutocomplete).

    class Meta:
        model = Emprestimo
        fields = ['livro', 'aluno', 'data_devolucao_prevista']
        widgets = {
            # MODIFICADO para usar o autocomplete do DAL
            'livro': dal.autocomplete.ModelSelect2(url='emprestimos:livro_autocomplete'),
            'aluno': dal.autocomplete.ModelSelect2(url='emprestimos:aluno_autocomplete'),
            
            'data_devolucao_prevista': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'data_devolucao_prevista': 'Data de Devolução Prevista',
            # Você pode adicionar labels para 'livro' e 'aluno' aqui se quiser
            'livro': 'Livro Disponível',
            'aluno': 'Aluno',
        }

    # O método clean para verificar a disponibilidade do livro ainda é útil
    # como uma validação extra no formulário, caso a busca não esteja 100% precisa,
    # ou para evitar problemas se alguém tentar submeter dados manualmente.
    def clean(self):
        cleaned_data = super().clean()
        livro = cleaned_data.get('livro')
        if livro and not livro.disponivel:
            self.add_error('livro', 'Este livro não está disponível para empréstimo.')
        return cleaned_data