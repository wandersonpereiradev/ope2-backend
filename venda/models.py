from django.db import models
from uuid import uuid4

# Create your models here.

class Venda(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    codigo_produto = models.IntegerField()
    quantidade_produto = models.IntegerField()
    preco_produto = models.DecimalField(decimal_places=2, max_digits=5)
    total_venda = models.DecimalField(decimal_places=2, max_digits=5)
