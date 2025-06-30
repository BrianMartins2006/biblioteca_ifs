# usuarios/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Modelo de usuário personalizado para o sistema de biblioteca, estendendo AbstractUser.
    Inclui campos para diferenciar entre Alunos e Bibliotecários, e a matrícula para Alunos.
    """
    is_bibliotecario = models.BooleanField(
        default=False,
        help_text='Indica se o usuário possui permissões de bibliotecário.'
    )
    matricula = models.CharField(
        max_length=20,
        unique=True,
        blank=True, 
        null=True,  
        help_text='Matrícula do aluno (se aplicável).'
    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username if self.username else f"{self.first_name} {self.last_name}".strip()

    def get_full_name(self):
        """
        Retorna o nome completo do usuário.
        """
        return super().get_full_name()
    
    def is_aluno(self):
        """
        Verifica se o usuário é um aluno.
        """
        return not self.is_bibliotecario

