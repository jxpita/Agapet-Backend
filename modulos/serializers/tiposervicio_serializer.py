from rest_framework import serializers
from modulos.models.tiposervicio import TipoServicio

#TipoServicio
class TipoServicioSerializer(serializers.ModelSerializer):
    subTipoServicio = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = TipoServicio
        fields = ('__all__')

