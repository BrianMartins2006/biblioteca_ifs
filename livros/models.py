# livros/models.py

from django.db import models

class Livro(models.Model):
    """
    Modelo que representa um livro na biblioteca.
    """
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    autor = models.CharField(
        max_length=100,
        verbose_name='Autor'
    )
    genero = models.CharField(
        max_length=50,
        blank=True, 
        null=True,
        verbose_name='Gênero'
    )
   
    disponivel = models.BooleanField(
        default=True,
        verbose_name='Disponível para Empréstimo'
    )

    curso_relacionado = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Curso ao qual o livro está mais relacionado (ex: Sistemas de Informação, Administração).',
        verbose_name='Curso Relacionado'
    )
    
    ano_publicacao = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Ano de Publicação'
    )

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo'] 

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

   