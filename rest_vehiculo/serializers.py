from django.db.models.base import Model
from rest_framework import serializers
from core.models import Vehiculo

class VehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Vehiculo
        fields =['patente','marca','modelo', 'categoria']