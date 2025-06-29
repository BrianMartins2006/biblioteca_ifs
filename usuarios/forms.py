# biblioteca_web/usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm # Base para criar formulário de usuário
from .models import CustomUser # Nosso modelo de usuário personalizado

class CustomUserCreationForm(UserCreationForm):
    # Campos adicionais para o registro, se houver
    # Exemplo: matricula. Se você quiser que o aluno preencha a matrícula no registro.
    # matricula = forms.CharField(max_length=20, required=False, help_text='Opcional. Sua matrícula de aluno.')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Exclua campos que não devem ser definidos pelo usuário no registro,
        # como is_bibliotecario, is_staff, is_superuser, etc.
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'matricula',) # Inclua campos que você quer no registro
        # Se você não quiser que a matrícula seja preenchida no registro, remova 'matricula' acima.
        # Se você não quiser nome/sobrenome no registro, remova 'first_name', 'last_name'.

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_bibliotecario = False # Garante que o novo usuário NÃO é um bibliotecário por padrão
        # user.matricula = self.cleaned_data.get('matricula') # Se você adicionou 'matricula' ao fields
        if commit:
            user.save()
        return user