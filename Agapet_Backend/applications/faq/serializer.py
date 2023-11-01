from rest_framework import serializers
from .models import Faq



""" class TemaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Tema
         fields= '__all__' """

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
         model = Faq
         fields= '__all__'



class FaqCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('pregunta', 'respuesta', 'idColaborador', 'idAdministrador')

    def create(self, validated_data):
        pregunta = Faq.objects.create(**validated_data)

        return pregunta

class FaqUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('pregunta', 'respuesta', 'is_active')

    def update(self, instance, validated_data):
        instance.pregunta = validated_data.get("pregunta", instance.pregunta)
        instance.respuesta = validated_data.get("respuesta", instance.respuesta)
        instance.is_active = validated_data.get("is_active", instance.is_active)

        instance.save()
        return instance
        

