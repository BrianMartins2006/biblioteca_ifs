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
        blank=True, # Opcional, se o gênero não for sempre obrigatório
        null=True,
        verbose_name='Gênero'
    )
    # No diagrama, 'disponivel' é um booleano.
    # Vamos usar um campo BooleanField com um valor padrão True.
    disponivel = models.BooleanField(
        default=True,
        verbose_name='Disponível para Empréstimo'
    )
    # O diagrama também menciona 'Consultar Livros por Curso'.
    # Podemos adicionar um campo de curso aqui, ou criar um modelo 'Curso' separado.
    # Por enquanto, vamos adicionar como um campo de texto simples para facilitar.
    curso_relacionado = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Curso ao qual o livro está mais relacionado (ex: Sistemas de Informação, Administração).',
        verbose_name='Curso Relacionado'
    )
    # Podemos adicionar o ano de publicação para filtros futuros (RF01)
    ano_publicacao = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Ano de Publicação'
    )

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo'] # Ordena os livros por título por padrão

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    # O método 'emprestar()' do diagrama será implementado na lógica do Empréstimo,
    # que irá alterar o status 'disponivel' do livro.