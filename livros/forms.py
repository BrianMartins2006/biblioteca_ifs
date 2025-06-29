# biblioteca_web/livros/forms.py

from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'genero', 'curso_relacionado', 'ano_publicacao', 'disponivel']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do Livro'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Nome do Autor'}),
            'genero': forms.TextInput(attrs={'placeholder': 'Ex: Ficção, Drama, Aventura'}),
            'curso_relacionado': forms.TextInput(attrs={'placeholder': 'Ex: Sistemas de Informação'}),
            'ano_publicacao': forms.NumberInput(attrs={'placeholder': 'Ex: 2023'}),
        }
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'genero': 'Gênero',
            'curso_relacionado': 'Curso Relacionado',
            'ano_publicacao': 'Ano de Publicação',
            'disponivel': 'Disponível para Empréstimo',
        }