from rest_framework import viewsets
from compras.api import serializers
from compras import models

class ComprasViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ComprasSerializer
    queryset = models.Compras.objects.all()