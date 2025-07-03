# biblioteca_web/usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    is_bibliotecario_field = forms.BooleanField(
        label='É Bibliotecário?',
        required=False,
        help_text='Marque esta opção para conceder permissões de bibliotecário a este usuário.'
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'matricula', 'is_bibliotecario_field',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_bibliotecario = self.cleaned_data['is_bibliotecario_field']
        if commit:
            user.save()
        return user

class CustomUserEditForm(forms.ModelForm):
    is_bibliotecario = forms.BooleanField(
        label='É Bibliotecário?',
        required=False,
        help_text='Marque se este usuário terá permissões de bibliotecário.'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'matricula', 'is_bibliotecario', 'is_active')