from rest_framework import viewsets
from modulos.models.notificacion import Notificacion
from modulos.serializers.notificacion_serializer import NotificacionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Personaliza la lógica para eliminar un objeto existente
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
