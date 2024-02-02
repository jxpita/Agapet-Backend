from rest_framework import viewsets
from modulos.models.evento import Evento
from modulos.serializers.evento_serializer import EventoSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def get_queryset(self):
        return Evento.objects.filter(estado='activado')
