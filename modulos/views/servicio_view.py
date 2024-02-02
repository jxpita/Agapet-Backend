from rest_framework import viewsets
from modulos.models.servicio import Servicio
from modulos.serializers.servicio_serializer import ServicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Personaliza la lógica para eliminar un objeto existente
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
