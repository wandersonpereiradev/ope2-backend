from rest_framework import viewsets
from usuarios.api import serializers
from usuarios import models

class UsuariosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.UsuariosSerializer
    queryset = models.Usuarios.objects.all()