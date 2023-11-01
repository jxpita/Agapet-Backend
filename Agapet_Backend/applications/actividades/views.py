from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Actividades
)
from .serializer import (
    ActividadesCreateSerializer,
    ActividadesSerializer,
    ActividadesUpdateSerializer,
    ActividadesSemanalesSerializer,
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)

from datetime import date
from datetime import datetime
# Create your views here.

class ActividadCreateView(CreateAPIView):
    serializer_class = ActividadesCreateSerializer

class ActividadListView(ListAPIView):
    serializer_class = ActividadesSerializer
    
    def get_queryset(self):
        actividades_list = Actividades.objects.all()
        for act in actividades_list:
            act.start =  act.start.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            act.end =  act.end.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        return actividades_list

class ActividadUpdateView(RetrieveUpdateAPIView):
    serializer_class = ActividadesUpdateSerializer
    queryset = Actividades.objects.all()

class ActividadDetailView(RetrieveAPIView):
    serializer_class = ActividadesSerializer
    queryset = Actividades.objects.all()

class ActividadSemanal:
    def __init__(self, actividad):
        self.actividad = actividad

class ActividadesSemanalesView(APIView):

    def get(self, request):
        semana = date.today().isocalendar().week
        anio = date.today().year

        actividades = Actividades.objects.all()
        acts = []
        for actividad in actividades:
            if actividad.start.isocalendar().week==semana and actividad.start.year==anio:
                act = ActividadSemanal(actividad=actividad)
                acts.append(act)

        acts.reverse()
        serializer = ActividadesSemanalesSerializer(acts, many = True)
        return Response(serializer.data)
