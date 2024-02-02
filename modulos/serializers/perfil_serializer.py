from rest_framework import serializers
from modulos.models.perfil import Perfil
from django.contrib.auth.models import User

#Usuario
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('fechaNacimiento', 'genero', 'pais', 'ciudad', 'direccion', 'fotoPerfil', 'tipo')


class UsuarioSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer(required=True)
    class Meta:
        model = User
        fields = ('__all__')

    def create(self, validated_data):
        perfil_data = validated_data.pop('perfil')
        user = User.objects.create(**validated_data)
        Perfil.objects.create(user=user, **perfil_data)
        return user

    def update(self, instance, validated_data):
        perfil_data = validated_data.pop('perfil')
        perfil = instance.perfil

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        if validated_data.get('password') is not None:
            instance.set_password(validated_data.get('password'))
        instance.save()

        perfil.fechaNacimiento = perfil_data.get('fechaNacimiento', perfil.fechaNacimiento)
        perfil.genero = perfil_data.get('genero', perfil.genero)
        perfil.pais = perfil_data.get('pais', perfil.pais)
        perfil.ciudad = perfil_data.get('ciudad', perfil.ciudad)
        perfil.direccion = perfil_data.get('direccion', perfil.direccion)
        perfil.fotoPerfil = perfil_data.get('fotoPerfil', perfil.fotoPerfil)
        perfil.save()

        return instance

