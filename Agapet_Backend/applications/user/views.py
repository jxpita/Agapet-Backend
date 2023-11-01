# Native
from django.shortcuts import render
# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import jwt, datetime

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    
)

# Serializers
from .serializer import (
    UserSerializer,
    RegisterSerializer,
    UserUpdateSerializer, 
    #UsuarioSerializer,
    UserSerializer2,
    AdminSerializer,
    ColaboradorSerializer,
    ColaboradorRegisterSerializer,
    AdoptanteRegisterSerializer,
    AdministradorRegisterSerializer,
    RecibePermisoSerializer,
    AdoptanteSerializer,
    CustomTokenObtainPairSerializer,
    AdministradorUpdateSerializer,
    ColaboradorUpdateSerializer,
    AdoptanteUpdateSerializer,
    RecibePermisoUpdateSerializer,

    NumeroAdoptantesSerializer,
)
# Models
from .models import User, Administrador, Colaborador, Adoptante, Recibe_Permiso

from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.db.models.functions import Trunc


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST)


class RegisterSecondView(CreateAPIView):
    serializer_class = RegisterSerializer
    """ def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors ,status= status.HTTP_400_BAD_REQUEST) """

class RegisterColaboradorView(CreateAPIView):
    serializer_class=ColaboradorRegisterSerializer

class RegisterAdoptanteView(CreateAPIView):
    serializer_class = AdoptanteRegisterSerializer

class ResgisterAdministradorView(CreateAPIView):
    serializer_class = AdministradorRegisterSerializer

class RecibePermisoView(CreateAPIView):
    serializer_class = RecibePermisoSerializer

class UserList(APIView):
    serializer_class = RegisterSerializer
    def get(self, request):
        #users = User.objects.all()
        users = User.objects.listar_usuarios()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)



class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializar = UserSerializer(request.user)
        return Response(serializar.data)
    

class Userupdate(APIView):
    def put(self, request):
        user = User.objects.get(iduser=request.user.iduser)
        serializer = UserUpdateSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminApiLista(ListAPIView):
    serializer_class = AdminSerializer
    def get_queryset(self):
        return Administrador.objects.all()

class ColaboradorApiLista(ListAPIView):

    serializer_class = ColaboradorSerializer
    def get_queryset(self):
        return Colaborador.objects.all()

class AdoptanteApiLista(ListAPIView):
    serializer_class = AdoptanteSerializer

    def get_queryset(self):
        return Adoptante.objects.all()


#REVISAR
#LISTAR USUARIOS INDIVIDUALES
class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all() 

class AdoptanteDetailView(RetrieveAPIView):
    serializer_class = AdoptanteSerializer
    queryset = Adoptante.objects.all()

class AdminDetailView(RetrieveAPIView):
    serializer_class = AdminSerializer
    queryset = Administrador.objects.all()

class ColaboradorDetailView(RetrieveAPIView):
    serializer_class = ColaboradorSerializer
    queryset = Colaborador.objects.all()

#ELIMINAR USUARIOS
class UserDeleteView(DestroyAPIView):
    serializer_class = UserSerializer #template
    queryset = User.objects.all() #model

#ACTUALIZAR USUARIOS 
class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AdministradorUpdateView(RetrieveUpdateAPIView):
    serializer_class = AdministradorUpdateSerializer
    queryset = Administrador.objects.all()

class ColaboradorUpdateView(RetrieveUpdateAPIView):
    serializer_class = ColaboradorUpdateSerializer
    queryset = Colaborador.objects.all()

class AdoptanteUpdateView(RetrieveUpdateAPIView):
    serializer_class = AdoptanteUpdateSerializer
    queryset = Adoptante.objects.all()

class RecibePermisoUpdateView(RetrieveUpdateAPIView):
    serializer_class = RecibePermisoUpdateSerializer
    queryset = Recibe_Permiso.objects.all()

class UserApiLista(ListAPIView):
    serializer_class = UserSerializer2
    def get_queryset(self):
        return User.objects.all()

class UserFilter(APIView):
    def get(self,request, user=None):
        users = User.objects.buscar_usuarios(user)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class NumeroAdoptante:
    def __init__(self, name, adoptantes):
        self.name = name
        self.adoptantes = adoptantes

class NumeroAdoptantesView(APIView):
    def get(self, request):
        m = {
        "1" :'enero',
        "2" :'febrero',
        "3" :'marzo',
        "4" :'abril',
        "5" :'mayo',
        "6" :'junio',
        "7" :'julio',
        "8" :'agosto',
        "9" :'septiembre',
        "10" :'octubre',
        "11" :'noviembre',
        "12" :'diciembre'
        }
        nums = []
        for x in range(12):
            current_month = date.today() + relativedelta(months=-x)
            mes = current_month.month
            anio = current_month.year
            month_name = m[str(mes)]
            adoptantes = Adoptante.objects.obtener_mes(mes, anio)
            count = 0
            for adoptante in adoptantes:
                count = count + 1
            num = NumeroAdoptante(name=month_name, adoptantes=count)
            nums.append(num) 
        nums.reverse()
        serializer = NumeroAdoptantesSerializer(nums, many = True)
        print(date.today().isocalendar().week)
        return Response(serializer.data)
        