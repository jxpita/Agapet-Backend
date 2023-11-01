from rest_framework import serializers
from .models import Curso, Tema_Curso, Respuesta, Pregunta

from applications.user.serializer import ColaboradorSerializer
from applications.user.serializer import AdminSerializer

#TEMA
class Tema_CursoSerializer(serializers.ModelSerializer):
    class Meta:
         model = Tema_Curso
         fields= '__all__'


class Tema_CursoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema_Curso
        fields = (
            'tema', 'descripcion', 'idColaborador', 'idAdministrador'
        )
    
    def create(self, validated_data):
        tema = Tema_Curso.objects.create(**validated_data)
        return tema

class Tema_CursoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema_Curso
        fields = (
            'tema', 'descripcion', 'is_active'
        )
    def update(self, instance, validated_data):
        instance.tema = validated_data.get("tema", instance.tema)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance

#CURSO
class CursoSerializer(serializers.ModelSerializer):
    idColaborador = ColaboradorSerializer()
    idAdministrador = AdminSerializer()
    class Meta:
         model = Curso
         fields= '__all__'

class CursoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'titulo', 'descripcion', 'url', 'minutos',
            'puntos', 'intentos', 'fecha', 'porcentaje',
            'imagen', 'adoptante', 'idColaborador', 'idAdministrador',
            'idtema'
        )

class CursoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'titulo', 'descripcion', 'url', 'minutos',
            'puntos', 'intentos', 'fecha', 'porcentaje',
            'imagen', 'adoptante', 'idtema', 'is_active'
        )

#CURSO_REALIZADO


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Respuesta
         fields= '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Pregunta
         fields= '__all__'

