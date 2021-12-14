from django.db import models
from uuid import uuid4

# Create your models here.

class Produtos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    codigo_produto = models.IntegerField()
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    categoria = models.CharField(max_length=255)
    preco_unitario = models.DecimalField(decimal_places=2, max_digits=5)


