# emprestimos/models.py

from django.db import models
from django.conf import settings # Importa o settings para acessar AUTH_USER_MODEL
from livros.models import Livro # Importa o modelo Livro

class Emprestimo(models.Model):
    """
    Modelo que representa um empréstimo de livro na biblioteca.
    Relaciona um Livro a um Usuário (Aluno) e registra as datas de empréstimo e devolução.
    """
    livro = models.ForeignKey(
        Livro,
        on_delete=models.PROTECT, # Protege o livro de ser deletado se houver empréstimos
        related_name='emprestimos',
        verbose_name='Livro'
    )
    # 'aluno' é uma ForeignKey para o nosso CustomUser
    aluno = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Usa o modelo de usuário definido em settings.py
        on_delete=models.PROTECT, # Protege o aluno de ser deletado se houver empréstimos
        related_name='emprestimos_realizados',
        verbose_name='Aluno'
    )
    data_emprestimo = models.DateTimeField(
        auto_now_add=True, # Define a data automaticamente na criação do empréstimo
        verbose_name='Data de Empréstimo'
    )
    data_devolucao_prevista = models.DateTimeField(
        verbose_name='Data de Devolução Prevista'
    )
    data_devolucao_real = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Data de Devolução Real'
    )
    # Adicionamos um status para o empréstimo, que pode ser 'emprestado', 'devolvido', 'atrasado'
    STATUS_CHOICES = [
        ('emprestado', 'Emprestado'),
        ('devolvido', 'Devolvido'),
        ('atrasado', 'Atrasado'), # Pode ser calculado dinamicamente ou definido por um bibliotecário
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='emprestado',
        verbose_name='Status do Empréstimo'
    )

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['-data_emprestimo'] # Ordena os empréstimos do mais recente para o mais antigo

    def __str__(self):
        return f"Empréstimo de '{self.livro.titulo}' para {self.aluno.username}"

    def save(self, *args, **kwargs):
        # Lógica para garantir que o livro seja marcado como indisponível ao ser emprestado
        if self.status == 'emprestado' and self.livro.disponivel:
            self.livro.disponivel = False
            self.livro.save()
        super().save(*args, **kwargs)

    def marcar_como_devolvido(self):
        """
        Marca o empréstimo como devolvido e atualiza a disponibilidade do livro.
        """
        self.data_devolucao_real = models.DateTimeField(auto_now_add=True).auto_now_add
        self.status = 'devolvido'
        self.livro.disponivel = True
        self.livro.save()
        self.save()

