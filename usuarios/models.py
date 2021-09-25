from django.db import models
from uuid import uuid4

# Create your models here.

class Usuarios(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    funcao = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    senha = models.IntegerField()
    is_admin = models.CharField(max_length=255)
