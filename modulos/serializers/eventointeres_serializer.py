from rest_framework import serializers
from modulos.models.eventointeres import EventoInteres

#EventoInteres
class EventoInteresSerializer(serializers.ModelSerializer):
    subEventoInteres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = EventoInteres
        fields = ('__all__')
