from django.shortcuts import render
from rest_framework import viewsets
from .models import Timeline, Timeline_fase, Fases
from .serializer import (
    FasesSerializer,
    FaseCreateSerializer, 
    FaseUpdateSerializer,

    TimelineSerializer, 
    TimelineCreateSerializer,
    TimelineUpdateSerializer,

    TimelineFaseSerializer,
    TimelineFaseCreateSerializer,
    TimelineFaseUpdateSerializer,
)
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    
)

# Create your views here.

#detail
class TimelineViewSet(APIView):
    def get(self, request,*args,**kwargs):
        queryset = Timeline.objects.all()
        id_user = self.request.query_params.get('idAdoptante',None)
        if id_user:
            queryset = queryset.filter(idAdoptante=id_user)
        serializers = TimelineSerializer(queryset, many=True)
        return Response(serializers.data)

class AdoptanteTimelineView(APIView):
    def get(self, request, pk):
        queryset = Timeline.objects.filter(idAdoptante=pk)
        serializers = TimelineSerializer(queryset, many=True)
        return Response(serializers.data)

#fase
class FaseListView(ListAPIView):
    serializer_class = FasesSerializer
    def get_queryset(self):
        return Fases.objects.all()

class FaseCreateView(CreateAPIView):
    serializer_class = FaseCreateSerializer

class FaseUpdateView(RetrieveUpdateAPIView):
    serializer_class = FaseUpdateSerializer
    queryset = Fases.objects.all()

#timeline
class TimelineListView(ListAPIView):
    serializer_class = TimelineSerializer
    def get_queryset(self):
        return Timeline.objects.all()

class TimelineDetailView(RetrieveAPIView):
    serializer_class = TimelineSerializer
    queryset = Timeline.objects.all()

class TimelineCreateView(CreateAPIView):
    serializer_class = TimelineCreateSerializer

class TimelineUpdateView(RetrieveUpdateAPIView):
    serializer_class = TimelineUpdateSerializer
    queryset = Timeline.objects.all()


#timeline fase
class Timeline_faseListView(ListAPIView):
    serializer_class = TimelineFaseSerializer
    def get_queryset(self):
        return Timeline_fase.objects.all()

class TimelineFaseCreateView(CreateAPIView):
    serializer_class = TimelineFaseCreateSerializer

class TimelineFaseUpdateView(RetrieveUpdateAPIView):
    serializer_class = TimelineFaseUpdateSerializer
    queryset = Timeline_fase.objects.all()