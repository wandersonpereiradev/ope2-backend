from rest_framework import viewsets
from servicos.api import serializers
from servicos import models

class ServicosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ServicosSerializer
    queryset = models.Servicos.objects.all()