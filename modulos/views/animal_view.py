from rest_framework import viewsets, status
from django.contrib.auth.admin import User
from modulos.models.animal import Animal
from modulos.serializers.animal_serializer import AnimalSerializer, CreateAnimalSerializer
from rest_framework.response import Response

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer()
    
    # Especifica el serializador a utilizar
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAnimalSerializer
        return AnimalSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Personaliza la lógica para eliminar un objeto existente
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AnimalesPorPerfilViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer()
    
    def get_queryset(self):
        perfil_id = self.kwargs.get('perfil_id')
        print("perfil_id:\t\n", perfil_id)
        userQuery = User.objects.all().filter(id=perfil_id)
        print("USERS:\t", userQuery)
        # Filtra los animales donde el usuarioResponsable es el usuario encontrado
        #print("OBJECTS:\t", Animal.objects.all())
        return Animal.objects.filter(usuarioResponsable=perfil_id)
    
    # Especifica el serializador a utilizar
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAnimalSerializer
        return AnimalSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Personaliza la lógica para eliminar un objeto existente
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    