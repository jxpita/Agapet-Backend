from rest_framework import serializers
from modulos.models.producto import Producto

#Producto
class ProductoSerializer(serializers.ModelSerializer):
    subProducto = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Producto
        fields = ('__all__')
