from rest_framework import viewsets
from modulos.models.alimento import Alimento
from modulos.serializers.alimento_serializer import AlimentoSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Personaliza la lógica para eliminar un objeto existente
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
