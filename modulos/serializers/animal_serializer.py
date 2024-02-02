from rest_framework import serializers
from modulos.models.animal import Animal
from django.contrib.auth.admin import User

#Animal
class AnimalSerializer(serializers.ModelSerializer):
    animal = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    usuarioResponsable_id = serializers.IntegerField()  # Permitir especificar el id del usuario responsable

    class Meta:
        model = Animal
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        # Extrae el ID del usuario responsable y busca la instancia del usuario
        usuario_id = validated_data.pop('usuarioResponsable_id')
        usuario = User.objects.get(id=usuario_id)
        
        # Asigna el usuario responsable al animal
        animal = Animal.objects.create(usuarioResponsable=usuario, **validated_data)
        return animal

class CreateAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'idAnimal',
            'nombreAnimal',
            'tipoAnimal',
            'raza',
            'alimento',
            'usuarioResponsable',
            'fechaRegistro',
            'fechaNacimiento',
            'sexo',
            'peso',
            'esterilizado',
            'frecuenciaPaseo',
            'estado',
            'descripcion',
            'tieneCollar',
            'tienePlaca',
            'origen',
            'personalidad',
            'disponibleParaAdopcion',
            'foto',
        ]