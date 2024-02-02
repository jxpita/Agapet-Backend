from rest_framework import serializers
from modulos.models.alimento import Alimento

#Alimento
class AlimentoSerializer(serializers.ModelSerializer):
    subAlimento = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Alimento
        fields = ('__all__')
