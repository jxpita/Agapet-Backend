from rest_framework import serializers
from modulos.models.servicio import Servicio

#Servicio
class ServicioSerializer(serializers.ModelSerializer):
    subServicio = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Servicio
        fields = ('__all__')
