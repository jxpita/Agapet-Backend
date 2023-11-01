from django.db import models

from applications.user.models import Colaborador, Administrador

# Create your models here.
class Actividades(models.Model):
    idActividades = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 700, blank = True, null = True)
    lugar = models.CharField(max_length = 300, blank = True, null = True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    colaborador = models.ForeignKey(Colaborador, blank = True, null=True, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, blank = True, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Actividades'
        verbose_name_plural = 'Actividades'
        db_table = 'Actividades'

    
