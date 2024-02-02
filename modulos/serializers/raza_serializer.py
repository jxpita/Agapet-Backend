from rest_framework import serializers
from modulos.models.raza import Raza

#Raza
class RazaSerializer(serializers.ModelSerializer):
    subRaza = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Raza
        fields = ('__all__')
