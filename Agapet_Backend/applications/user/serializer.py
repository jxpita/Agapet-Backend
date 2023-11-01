from django.db import models
from django.utils import timezone
import datetime

from rest_framework import serializers
from .models import (User, Administrador, Colaborador, Adoptante, Recibe_Permiso)
from applications.Permisos.models import Permiso
from applications.Permisos.serializer import PermisoSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'name': self.user.name})
        data.update({'id': self.user.iduser})
        data.update({'user_type': self.user.user_type})
        if(Colaborador.objects.filter(user=self.user).values()):
            data.update({'idColaborador': Colaborador.objects.filter(user=self.user).values()[0]['idColaborador']})
        if(Administrador.objects.filter(user=self.user).values()):
            data.update({'idAdministrador': Administrador.objects.filter(user=self.user).values()[0]['idAdministrador']})
        if(Adoptante.objects.filter(user=self.user).values()):
            data.update({'idAdoptante': Adoptante.objects.filter(user=self.user).values()[0]['idAdoptante']})
        return data


# Serializer from model user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['iduser','name', 'lastname','email','phone','direction', 'age', 'gender', 'last_login', 'is_active']



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['iduser','name', 'lastname','email','password','phone','direction', 'age', 'gender']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Administrador
        fields = ('__all__')
    

class AdoptanteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Adoptante
        fields = ('__all__')
    

class Recibe_PermisoSerializer(serializers.ModelSerializer):
    permiso = PermisoSerializer()
    class Meta:
        model = Recibe_Permiso
        #fields = ('__all__')  
        exclude = ('colaborador',)  

#TODOS VAN A SER UPDATE     
class RecibePermisoSerializer(serializers.ModelSerializer):
    permiso = serializers.PrimaryKeyRelatedField(queryset=Permiso.objects.all())
    colaborador = serializers.PrimaryKeyRelatedField(queryset=Colaborador.objects.all())
    class Meta:
        model = Recibe_Permiso
        fields = ('__all__')

class ColaboradorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    permisos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Colaborador
        fields = ('__all__')
    
    def get_permisos(self, obj):
        return Recibe_PermisoSerializer(obj.colaborador_to_permiso.all(), many=True).data

class ColaboradorRegisterSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    permisos = PermisoSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Colaborador
        fields = ('__all__')
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user_clb(**user_data)
        colaborador = Colaborador.objects.create(user=user, **validated_data)
        permisos = Permiso.objects.all()
        for permiso_data in permisos:
            Recibe_Permiso.objects.create(colaborador=colaborador, permiso = permiso_data, estado_permiso=False, date_received= timezone.now())
        return colaborador
        

class AdoptanteRegisterSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()

    class Meta: 
        model = Adoptante
        fields = ('__all__')
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user_adp(**user_data)
        adoptante = Adoptante.objects.create(user=user, **validated_data)
        return adoptante

class AdministradorRegisterSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()

    class Meta:
        model = Administrador
        fields = ('__all__')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_superuser(**user_data)
        administrador = Administrador.objects.create(user = user, **validated_data)
        return administrador
        
""" class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['iduser', 'name', 'lastname','phone','direction', 'age', 'gender', 'last_login', 'is_active'] """

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['iduser', 'name', 'lastname','phone','direction', 'age', 'gender', 'last_login', 'is_active']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.lastname = user_data.get('lastname', instance.lastname)
        instance.phone = user_data.get('phone', instance.phone)
        instance.direction = user_data.get('direction', instance.direction)
        instance.age = user_data.get('age', instance.age)
        instance.gender =  user_data.get('gender', instance.gender)
        instance.last_login = user_data.get('last_login', instance.last_login)
        instance.is_active = user_data.get('is_active', instance.is_active)

        instance.save()
        return instance()
    
class AdministradorUpdateSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()
    
    class Meta:
        model = Administrador
        fields = ('__all__')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.name = user_data.get('name', user.name)
        user.lastname = user_data.get('lastname', user.lastname)
        user.phone = user_data.get('phone', user.phone)
        user.direction = user_data.get('direction', user.direction)
        user.age = user_data.get('age', user.age)
        user.gender =  user_data.get('gender', user.gender)
        user.last_login = user_data.get('last_login', user.last_login)
        user.is_active = user_data.get('is_active', user.is_active)

        user.save()
        instance.save()
        return instance


class RecibePermisoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recibe_Permiso
        fields = ['id','date_received','estado_permiso']

    def update(self, instance, validated_data):
        instance.date_received = validated_data.get('date_received', instance.date_received)
        instance.estado_permiso = validated_data.get('estado_permiso', instance.estado_permiso)
        instance.save()
        return instance



class ColaboradorUpdateSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()

    class Meta:
        model = Colaborador
        exclude = ('permisos',)  

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')

        user = instance.user
        user.name = user_data.get('name', user.name)
        user.lastname = user_data.get('lastname', user.lastname)
        user.phone = user_data.get('phone', user.phone)
        user.direction = user_data.get('direction', user.direction)
        user.age = user_data.get('age', user.age)
        user.gender = user_data.get('gender', user.gender)
        user.last_login = user_data.get('last_login', user.last_login)
        user.is_active = user_data.get('is_active', user.is_active)

        user.save()
        instance.save()
        return instance

class AdoptanteUpdateSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer()
    class Meta:
        model = Adoptante
        fields = ('__all__')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')

        user = instance.user
        user.name = user_data.get('name', user.name)
        user.lastname = user_data.get('lastname', user.lastname)
        user.phone = user_data.get('phone', user.phone)
        user.direction = user_data.get('direction', user.direction)
        user.age = user_data.get('age', user.age)
        user.gender = user_data.get('gender', user.gender)
        user.last_login = user_data.get('last_login', user.last_login)
        user.is_active = user_data.get('is_active', user.is_active)

        instance.points = validated_data.get('points', instance.points)
        instance.imagen64 = validated_data.get('imagen64', instance.imagen64)

        user.save()
        instance.save()
        return instance

class UserSerializer2(serializers.ModelSerializer):

    active = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ['iduser','name','email','phone','direction', 'age', 'active']



    

class NumeroAdoptantesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    adoptantes = serializers.IntegerField()



    

