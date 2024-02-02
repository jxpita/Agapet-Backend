from django.db import models
from django.contrib.auth.admin import User
from modulos.models.tipoanimal import TipoAnimal
from modulos.models.alimento import Alimento
from modulos.models.raza import Raza
from datetime import datetime

# Create your models here.
class Animal(models.Model):
    idAnimal = models.AutoField(primary_key=True)
    nombreAnimal = models.CharField(max_length=25)
    tipoAnimal = models.CharField(max_length=15, choices=(('perro', 'Perro'), ('gato', 'Gato')))
    #tipoAnimal = models.ForeignKey(TipoAnimal, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, blank=True, null=True)
    alimento = models.CharField(max_length=15, choices=(('dog chown', 'Dog Chow'), ('procan', 'Procan')), default= 'Procan')
    usuarioResponsable = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fechaRegistro = models.DateTimeField(default=datetime.now())
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=15, choices=(('macho', 'Macho'), ('hembra', 'Hembra')))
    peso = models.FloatField()
    esterilizado = models.BooleanField()
    frecuenciaPaseo = models.PositiveSmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=15, choices= (('activo', 'Activo'), ('perdido', 'Perdido'), ('fallecido', 'Fallecido')), default='Activo')
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    tieneCollar = models.BooleanField(default=False, blank=True, null=True)
    tienePlaca = models.BooleanField(default=False, blank=True, null=True)
    origen = models.CharField(max_length=15, choices= (('adoptado', 'Adoptado'), ('rescatado', 'Rescatado'), ('comprado', 'Comprado')))
    personalidad = models.CharField(max_length=15, choices= (('sociable', 'Sociable'), ('deportista', 'Deportista'), ('solitario', 'Solitario'), ('niñero', 'Niñero')), blank=True, null=True)
    disponibleParaAdopcion = models.BooleanField(default=False, blank=True, null=True)
    foto = models.ImageField(upload_to='static/img/animales/', blank=True, null=True)
    
    def __str__(self):
      return self.nombreAnimal


    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
        db_table = 'Animal'
