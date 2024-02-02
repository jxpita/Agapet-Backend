from django.db import models
from modulos.models.tiposervicio import TipoServicio
from django.contrib.auth.models import User
from modulos.models.animal import Animal
from modulos.models.producto import Producto


# Create your models here.
class Servicio(models.Model):
    # Fields
    idServicio = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=50)
    tipoServicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, blank = True)
    descripcion = models.CharField(max_length=150, blank = True, null = True)
    fechaServicio = models.DateTimeField()
    fechaProximoServicio = models.DateField(blank = True, null = True)
    lugar = models.CharField(max_length=50, blank = True, null = True)
    precio = models.PositiveSmallIntegerField(blank = True, null = True)
    descuento = models.PositiveSmallIntegerField(blank = True, null = True)

    def __str__(self):
      return self.servicio


    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        db_table = 'Servicio'
