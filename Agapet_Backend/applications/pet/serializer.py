from rest_framework import serializers
from .models import Animal, Mascota, Vacunado, Vacuna
from applications.user.serializer import UserSerializer, AdoptanteSerializer, ColaboradorSerializer, AdminSerializer
from applications.user.models import Adoptante
from applications.vacuna.serializer import VacunaSerializer

from django.utils import timezone
import datetime

#Animal
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
         model = Animal
         fields= '__all__'

#Mascota
class MascotaSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    adoptante = AdoptanteSerializer()
    vacunas = serializers.SerializerMethodField(read_only = True)

    class Meta:
         model = Mascota
         fields= '__all__'
    
    def get_vacunas(self, obj):
        return Vacunado_Serializer(obj.mascota_to_vacuna.all(), many = True).data

class MascotaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = [
            'idpet', 
            'colaborador',
            'administrador', 
            'animal', 'nombre', 
            'genero', 'estado',
            'descripcion', 'image64', 
            'edad', 'peso', 'comida', 
            'deportivo', 'jugueton', 'sociable', 
            'miedoso', 'esterilizado', 'fecha_esterilizado', 
            'lugar_esterilizado', 'descripcion_esterilizado', 
            'desparacitado', 'fecha_desparacitado', 
            'lugar_desparacitado', 'descripcion_desparacitado' ]

    def create(self, validated_data):
        mascota = Mascota.objects.create_mascota(**validated_data)
        return mascota


class MascotaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        exclude = ('administrador', 'colaborador', 'fecha_creacion', 'vacunas', 'estado')
    
    def update(self, instance, validated_data):
        adoptante_data = validated_data.pop('adoptante')

        instance.animal = validated_data.get('animal', instance.animal)
        instance.adoptante = adoptante_data
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.genero = validated_data.get('genero', instance.genero)
        #instance.estado = validated_data.get('estado', instance.estado)
        instance.adopted = validated_data.get('adopted', instance.adopted)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.image64 = validated_data.get('image64', instance.image64)
        instance.edad = validated_data.get('edad', instance.edad)
        instance.peso = validated_data.get('peso', instance.peso)
        instance.comida = validated_data.get('comida', instance.comida)
        instance.deportivo = validated_data.get('deportivo', instance.deportivo)
        instance.jugueton = validated_data.get('jugueton', instance.jugueton)
        instance.sociable = validated_data.get('sociable', instance.sociable)
        instance.miedoso = validated_data.get('miedoso', instance.miedoso)
        instance.esterilizado = validated_data.get('esterilizado', instance.esterilizado)
        instance.fecha_esterilizado = validated_data.get('fecha_esterilizado', instance.fecha_esterilizado)
        instance.lugar_esterilizado = validated_data.get('lugar_esterilizado', instance.lugar_esterilizado)
        instance.descripcion_esterilizado = validated_data.get('descripcion_esterilizado', instance.descripcion_esterilizado)
        instance.desparacitado = validated_data.get('desparacitado', instance.desparacitado)
        instance.fecha_desparacitado = validated_data.get('fecha_desparacitado', instance.fecha_desparacitado)
        instance.lugar_desparacitado = validated_data.get('lugar_desparacitado', instance.lugar_desparacitado)
        instance.descripcion_desparacitado = validated_data.get('descripcion_desparacitado', instance.descripcion_desparacitado)

        instance.is_active = validated_data.get('is_active', instance.is_active)

        if(instance.adopted=='AD'):
            instance.estado = 'N'
        else:
            instance.estado = 'S'
        
        if(instance.adoptante):
            instance.estado='N'
        else:
            instance.estado = 'S'
        
        instance.save()
        return instance

#Vacunado
class VacunadoSerializer(serializers.ModelSerializer):
    vacuna = serializers.PrimaryKeyRelatedField(queryset = Vacuna.objects.all())
    mascota = serializers.PrimaryKeyRelatedField(queryset = Mascota.objects.all())

    class Meta:
        model = Vacunado
        fields = ('__all__')
        #exclude = ('mascota',)  

class Vacunado_Serializer(serializers.ModelSerializer):
    vacuna = VacunaSerializer()
    
    class Meta:
        model = Vacunado
        exclude = ('mascota',)  
    
class VacunadoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacunado
        fields = ('__all__')
    
    def update(self, instance, validated_data):
        instance.vacuna = validated_data.get("vacuna", instance.vacuna)
        instance.descripcion_vacunacion = validated_data.get('descripcion_vacunacion', instance.descripcion_vacunacion)
        instance.imagen64 = validated_data.get('imagen64', instance.imagen64)
        instance.lugar_vacunacion = validated_data.get('lugar_vacunacion', instance.lugar_vacunacion)
        instance.fecha_vacunacion = validated_data.get('fecha_vacunacion', instance.fecha_vacunacion)
        instance.save()
        return instance
