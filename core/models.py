from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

        class Meta:
            verbose_name = 'Categoria'
            verbose_name_plural = 'Categorias'

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Editoras'

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Autores'

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros')
    autores = models.ManyToManyField(Autor, related_name='livros')

    def __str__(self):
        return f"{self.titulo} ({self.editora})"

    class Meta:
        verbose_name_plural = 'Livros'

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'


    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)

    def __str__(self):
        return f"{self.usuario} - {self.get_status_display()}"

    class Meta:
        verbose_name_plural = 'Compras'

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.compra} - {self.livro}"

    class Meta:
        verbose_name_plural = 'Itens de Compra'