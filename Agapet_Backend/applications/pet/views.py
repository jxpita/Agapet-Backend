from django.shortcuts import render
from rest_framework import viewsets
from .models import Animal, Mascota, Vacunado
from .serializer import (
    AnimalSerializer, 
    MascotaSerializer, 
    MascotaCreateSerializer, 
    MascotaUpdateSerializer,
    VacunadoSerializer,
    VacunadoUpdateSerializer,
    
)
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)
# Create your views here.

class MascotaViewSet(viewsets.ModelViewSet):
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()

class UsuarioMascotaViewSet(APIView):
    def get(self, request,pk):
        adoptante = Mascota.objects.get(adoptante=pk)
        serializers = MascotaSerializer(adoptante, many=False)
        return Response(serializers.data)

class UsuarioMascotaView(APIView):
    def get(self, request, pk):
        queryset = Mascota.objects.filter(adoptante=pk)
        serializers = MascotaSerializer(queryset, many=True)
        return Response(serializers.data)
       

class MascotaCreateView(CreateAPIView):
    serializer_class = MascotaCreateSerializer

class MascotaUpdateView(RetrieveUpdateAPIView):
    serializer_class = MascotaUpdateSerializer
    queryset = Mascota.objects.all()

class MascotaListView(ListAPIView):
    serializer_class = MascotaSerializer

    def get_queryset(self):
        return Mascota.objects.all()

class MascotaDetailView(RetrieveAPIView):
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()

#Animal
class AnimalListView(ListAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

class AnimalCreateView(CreateAPIView):
    serializer_class = AnimalSerializer

#VACUNAS

class VacunadoView(CreateAPIView):
    serializer_class = VacunadoSerializer

class VacunadoUpdateView(RetrieveUpdateAPIView):
    serializer_class = VacunadoUpdateSerializer
    queryset = Vacunado.objects.all()
