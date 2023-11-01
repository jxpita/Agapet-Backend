from rest_framework import serializers
from .models import Timeline, Fases, Timeline_fase

from django.utils import timezone
import datetime
from datetime import datetime


class FasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fases
        fields = ('__all__')


class FaseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fases
        #fields = ('__all__')
        fields = ('nombre', 
        'descripcion','estado', 'fecha_inactivacion', 
        'idColaborador', 'idAdministrador')

    def create(self, validated_data):
        timelines = Timeline.objects.all()

        fase = Fases.objects.create_fase(**validated_data)

        for timeline in timelines:
            timeline_fase = Timeline_fase.objects.create(timeline=timeline, fase=fase, estado="E")
            timeline.fases.add()
        return fase

class FaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fases
        fields = ('nombre', 'descripcion','estado', 'fecha_inactivacion', 'is_active')
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.fecha_inactivacion = validated_data.get('fecha_inactivacion', instance.fecha_inactivacion)

        instance.save()
        return instance


#TIMELINE FASE
#crear las fases dentro del timeline
class Timeline_faseSerializer(serializers.ModelSerializer):
    fase = FasesSerializer()
    class Meta:
        model = Timeline_fase
        exclude = ('timeline',)

#para listar las timeline_fases
class TimelineFaseSerializer(serializers.ModelSerializer):
    fase = serializers.PrimaryKeyRelatedField(queryset=Fases.objects.all())
    timeline = serializers.PrimaryKeyRelatedField(queryset=Timeline.objects.all())
    class Meta:
        model = Timeline_fase
        fields = ('__all__')

class TimelineFaseCreateSerializer(serializers.ModelSerializer):
    fase = serializers.PrimaryKeyRelatedField(queryset=Fases.objects.all())
    timeline = serializers.PrimaryKeyRelatedField(queryset=Timeline.objects.all())
    class Meta:
        model = Timeline_fase
        fields = ('estado', 'comentarios', 'fecha_inicio', 'fecha_final', 'fase', 'timeline')
    def create(self, validated_data):
        fase = validated_data.pop('fase')
        nombre = fase.nombre
        if(nombre=="Formulario"):
            estado_i=validated_data.pop('estado')
            estado = 'A'
            fecha_inicio_i = validated_data.pop('fecha_inicio')
            fecha_final_i = validated_data.pop('fecha_final')
            timelinefase = Timeline_fase.objects.create(fecha_inicio="{:%Y-%m-%d}".format(datetime.now()),fecha_final="{:%Y-%m-%d}".format(datetime.now()),fase=fase,estado=estado,**validated_data)
        else:
            timelinefase = Timeline_fase.objects.create(fase=fase,**validated_data)
        
        return timelinefase
        
    
class TimelineFaseUpdateSerializer(serializers.ModelSerializer):
    class Meta: #, 'fase', 'timeline'
        model = Timeline_fase
        fields = ('estado', 'comentarios', 'fecha_inicio', 'fecha_final', 'is_active')
    
    def update(self, instance, validated_data):
        instance.estado = validated_data.get('estado', instance.estado)
        instance.comentarios = validated_data.get('comentarios', instance.comentarios)
        instance.fecha_inicio = validated_data.get('fecha_inicio', instance.fecha_inicio)
        instance.fecha_final = validated_data.get('fecha_final', instance.fecha_final)
        instance.is_active = validated_data.get('is_active' ,instance.is_active)
        instance.save()
        return instance

#TIMELINE
#en timeline create, se crean de una las fases por cada timeline
class TimelineCreateSerializer(serializers.ModelSerializer):
    fases = FasesSerializer(many = True, required = False, read_only = True)
    class Meta:
        model = Timeline
        fields = ('fases',
        'descripcion','estado','fecha_inicio',
        'fecha_final','idAdoptante','idpet', 
        'idColaborador', 'idAdministrador')

    def create(self, validated_data):
        timeline = Timeline.objects.create(**validated_data)
        fases = Fases.objects.all()
        for fase_data in fases:
            Timeline_fase.objects.create(timeline=timeline, fase=fase_data, estado="E", fecha_inicio = timezone.now())
        return timeline


class TimelineSerializer(serializers.ModelSerializer):
    fases = serializers.SerializerMethodField(read_only = True)
    class Meta:
         model = Timeline
         fields= ('__all__')
    
    def get_fases(self, obj):
        return Timeline_faseSerializer(obj.timeline_to_fases.all(), many = True).data

#update
class TimelineUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ('descripcion','estado','fecha_inicio','fecha_final', 'is_active')

    def update(self, instance, validated_data):
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.fecha_inicio = validated_data.get('fecha_inicio', instance.fecha_inicio)
        instance.fecha_final = validated_data.get('fecha_final', instance.fecha_final)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.save()
        return instance



