from rest_framework import serializers
from .models import Vacuna
from .managers import VacunaManager

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Vacuna
         fields= ('__all__')

class VacunaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['vacuna_id','idAdministrador', 'idColaborador','nombre_vacuna','descripcion_vacuna']

    def create(self, validated_data):
        vacuna = Vacuna.objects.create_vacuna(**validated_data)
        return vacuna

class VacunaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
         model = Vacuna
         fields= ['vacuna_id','nombre_vacuna','descripcion_vacuna','is_active']
    
    def update(self, instance, validated_data):
        instance.nombre_vacuna = validated_data.get('nombre_vacuna',instance.nombre_vacuna)
        instance.descripcion_vacuna = validated_data.get('descripcion_vacuna', instance.descripcion_vacuna)
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.save()
        return instance
