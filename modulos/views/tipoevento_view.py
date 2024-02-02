from rest_framework import viewsets
from modulos.models.tipoevento import TipoEvento
from modulos.serializers.tipoevento_serializer import TipoEventoSerializer

class TipoEventoViewSet(viewsets.ModelViewSet):
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Personaliza la lógica para eliminar un objeto existente
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
