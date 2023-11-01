from django.db import models
from django.utils import timezone
import datetime
from datetime import datetime


from rest_framework import serializers
from .models import (
    Actividades
)

from applications.user.serializer import (
    AdminSerializer,
    ColaboradorSerializer,
)

from applications.user.models import Administrador, Colaborador

#Actividades
class ActividadesSerializer(serializers.ModelSerializer):
    colaborador = ColaboradorSerializer()
    administrador = AdminSerializer()
    class Meta:
        model = Actividades
        fields = ('__all__')

class ActividadesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = ('__all__')
    
    def create(self, validated_data):
        start=validated_data.pop('start')
        end=validated_data.pop('end')
        instance = self.Meta.model(**validated_data)
        instance.__setattr__("start", start.strftime("%Y-%m-%dT%H:%M:%S.000Z"))
        instance.__setattr__("end", end.strftime("%Y-%m-%dT%H:%M:%S.000Z"))

        instance.save()
        return instance
    

class ActividadesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = ('__all__')

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.lugar = validated_data.get("lugar", instance.lugar)
        instance.start = validated_data.get("start", instance.start)
        instance.end = validated_data.get("end", instance.end)
        instance.is_active = validated_data.get("is_active", instance.is_active)

        instance.save()
        return instance


class ActividadesSemanalesSerializer(serializers.Serializer):
    actividad = ActividadesSerializer()