from rest_framework import serializers
from modulos.models.tipoevento import TipoEvento

#TipoEvento
class TipoEventoSerializer(serializers.ModelSerializer):
    subTipoEvento = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = TipoEvento
        fields = ('__all__')
