from django.db.models import F
from django.contrib.auth import get_user_model
from django.db import models

from .livro import Livro


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, related_name="compras"
    )
    status = models.IntegerField(
        choices=StatusCompra.choices, default=StatusCompra.CARRINHO
    )

    @property
    def total(self):
        queryset = self.itens.all().aggregate(
            total=models.Sum(F("livro__preco") * F("quantidade"))
        )
        return queryset["total"]

    def __str__(self):
        return f"{self.usuario} - {self.get_status_display()}"

    class Meta:
        verbose_name_plural = "Compras"


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.compra} - {self.livro}"

    class Meta:
        verbose_name_plural = "Itens de Compra"
