from django.db import models
from django.utils import timezone
import datetime

from rest_framework import serializers
from .models import (Permiso)
from applications.user.models import Colaborador, Recibe_Permiso

class PermisoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permiso
        fields = ('__all__')

    def create(self, validated_data):
        colaboradores = Colaborador.objects.all()

        permiso = Permiso.objects.create(**validated_data)

        for colaborador in colaboradores:
            recibido = Recibe_Permiso.objects.create(permiso=permiso, colaborador=colaborador, date_received=timezone.now(), estado_permiso=False)
            colaborador.permisos.add()

        return permiso

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance





""" 
def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user_clb(**user_data)
        colaborador = Colaborador.objects.create(user=user, **validated_data)
        permisos = Permiso.objects.all()
        for permiso_data in permisos:
            Recibe_Permiso.objects.create(colaborador=colaborador, permiso = permiso_data, estado_permiso=False, date_received= timezone.now())
        return colaborador """