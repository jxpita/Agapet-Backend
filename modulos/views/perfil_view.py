from rest_framework import viewsets
from modulos.models.perfil import Perfil
from django.contrib.auth.models import User
from modulos.serializers.perfil_serializer import UsuarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from modulos import serializers
from rest_framework import permissions


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.AllowAny,)

class NombreUsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username:
            return queryset.filter(username=username)
        return queryset

class UsuarioColaboradorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(perfil__tipo='CO')
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.AllowAny,)

class UsuarioClienteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(perfil__tipo='C')
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.AllowAny,)

class CreateUserView(APIView):
    model = User
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
