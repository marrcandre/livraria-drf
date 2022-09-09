from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
    rg = models.CharField(max_length=7, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.username}"
