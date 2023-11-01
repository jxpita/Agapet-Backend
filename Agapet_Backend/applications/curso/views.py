from django.shortcuts import render
from rest_framework import viewsets
from .models import Curso, Tema_Curso, Pregunta, Respuesta
from .serializer import (
    CursoSerializer,
    CursoCreateSerializer,
    CursoUpdateSerializer,

    Tema_CursoSerializer, 
    Tema_CursoCreateSerializer,
    Tema_CursoUpdateSerializer,

    PreguntaSerializer, 
    RespuestaSerializer
)


# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    RetrieveAPIView
)
# Create your views here.

#Tema_Curso
class TemaCursoList(APIView):
    def get(self, request):
        tema = Tema_Curso.objects.all()
        serializer = Tema_CursoSerializer(tema, many=True)
        return Response(serializer.data)

class TemaCursoCreateView(CreateAPIView):
    serializer_class = Tema_CursoCreateSerializer

class TemaCursoUpdateView(RetrieveUpdateAPIView):
    serializer_class = Tema_CursoUpdateSerializer
    queryset = Tema_Curso.objects.all()

class TemaCursoDetailView(RetrieveAPIView):
    serializer_class = Tema_CursoSerializer
    queryset = Tema_Curso.objects.all()

#Cursos
class CursoList(APIView):
    def get(self, request):
        curso = Curso.objects.all()
        serializer = CursoSerializer(curso, many=True)
        return Response(serializer.data)

class CursoCreateView(CreateAPIView):
    serializer_class = CursoCreateSerializer

class CursoUpdateView(RetrieveUpdateAPIView):
    serializer_class = CursoUpdateSerializer
    queryset = Curso.objects.all()

class CursoDetailView(RetrieveAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()


#Preguntas
class PreguntaList(APIView):
    def get(self, request):
        pregunta = Pregunta.objects.all()
        serializer = PreguntaSerializer(pregunta, many=True)
        return Response(serializer.data)

class RespuestaList(APIView):
    def get(self, request):
        respuesta = Respuesta.objects.all()
        serializer = RespuestaSerializer(respuesta, many=True)
        return Response(serializer.data)

class TemaiewSet(APIView):
    def get(self, request,*args,**kwargs):
        queryset = Tema_Curso.objects.all()
        idtema = self.request.query_params.get('idcurso',None)
        if idtema:
            queryset = queryset.filter(idcurso=idtema)
        serializers = Tema_CursoSerializer(queryset, many=True)
        return Response(serializers.data)
