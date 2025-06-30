# biblioteca_web/emprestimos/forms.py

from django import forms
from .models import Emprestimo
from livros.models import Livro
from usuarios.models import CustomUser
import dal.autocomplete 

class EmprestimoForm(forms.ModelForm):
  
    class Meta:
        model = Emprestimo
        fields = ['livro', 'aluno', 'data_devolucao_prevista']
        widgets = {
            'livro': dal.autocomplete.ModelSelect2(url='emprestimos:livro_autocomplete'),
            'aluno': dal.autocomplete.ModelSelect2(url='emprestimos:aluno_autocomplete'),
            
            'data_devolucao_prevista': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'data_devolucao_prevista': 'Data de Devolução Prevista',
            'livro': 'Livro Disponível',
            'aluno': 'Aluno',
        }

    def clean(self):
        cleaned_data = super().clean()
        livro = cleaned_data.get('livro')
        if livro and not livro.disponivel:
            self.add_error('livro', 'Este livro não está disponível para empréstimo.')
        return cleaned_data