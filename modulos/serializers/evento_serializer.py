from rest_framework import serializers
from modulos.models.evento import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'  # Seleccionamos todos los campos del modelo
