# biblioteca_web/usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser 

class CustomUserCreationForm(UserCreationForm):
 

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'matricula',) 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_bibliotecario = False 
        if commit:
            user.save()
        return user