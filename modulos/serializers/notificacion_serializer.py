from rest_framework import serializers
from modulos.models.notificacion import Notificacion

#Notificacion
class NotificacionSerializer(serializers.ModelSerializer):
    subNotificacion = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Notificacion
        fields = ('__all__')
