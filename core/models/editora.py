from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Editoras"
