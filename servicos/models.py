from django.db import models
from uuid import uuid4
from datetime import *
from time import *

class Servicos(models.Model):
    id_servico = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    numero_servico = models.IntegerField
    cliente_id = models.CharField(max_length=255)
    veiculo = models.CharField(max_length=255)
    servico_realizado= models.CharField(max_length=255)
    data_cadastro = models.DateTimeField
    data_servico = models.DateTimeField