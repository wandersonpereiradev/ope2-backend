from rest_framework import serializers
from compras import models

class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Compras
        fields = '__all__'