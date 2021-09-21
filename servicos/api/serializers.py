from rest_framework import serializers
from servicos import models

class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servicos
        fields = '__all__'