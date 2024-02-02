from rest_framework import viewsets
from modulos.models.eventointeres import EventoInteres
from modulos.serializers.eventointeres_serializer import EventoInteresSerializer

class EventoInteresViewSet(viewsets.ModelViewSet):
    queryset = EventoInteres.objects.all()
    serializer_class = EventoInteresSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Personaliza la lógica para eliminar un objeto existente
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
