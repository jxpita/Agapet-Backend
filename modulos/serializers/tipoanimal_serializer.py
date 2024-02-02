from rest_framework import serializers
from modulos.models.tipoanimal import TipoAnimal

#TipoAnimal
class TipoAnimalSerializer(serializers.ModelSerializer):
    subTipoAnimal = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = TipoAnimal
        fields = ('__all__')

