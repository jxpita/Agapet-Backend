from rest_framework import viewsets
from modulos.models.tipoanimal import TipoAnimal
from modulos.serializers.tipoanimal_serializer import TipoAnimalSerializer

class TipoAnimalViewSet(viewsets.ModelViewSet):
    queryset = TipoAnimal.objects.all()
    serializer_class = TipoAnimalSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Personaliza la lógica para eliminar un objeto existente
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
