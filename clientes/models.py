from django.db import models
from uuid import uuid4

class Clientes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.EmailField
    contato = models.CharField(max_length=255)
    veiculo = models.CharField(max_length=255)
    placa = models.CharField(max_length=255)

