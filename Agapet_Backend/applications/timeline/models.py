from django.db import models
from applications.user.models import User, Administrador, Colaborador, Adoptante
from applications.pet.models import Mascota
from .managers import FaseManager

from django.utils import timezone
import datetime

# Create your models here.

class Fases(models.Model):
    """ tipo_fase = (
        ('F', 'Formulario'),
        ('W', 'Entrevista por whatsapp'),
        ('V', 'Visita al domicilio'),
        ('C', 'Firma de contrato'),
        ('E', 'Entrega'),
        ('S', 'Seguimiento')
    ) """

    opcion_estado = (
        ('A', 'Activa'),
        ('I', 'Inactiva')
    )

    idFase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    """tipo = models.CharField(max_length=1, choices=tipo_fase)""" 
    descripcion = models.CharField(max_length=200, null = True, blank = True)
    estado = models.CharField(max_length=1, choices=opcion_estado)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_inactivacion = models.DateField(blank=True, null=True)
    idColaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, blank = True, null = True)
    idAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, blank = True, null = True)

    is_active = models.BooleanField(default = True)

    objects=FaseManager()

    class Meta:
        verbose_name='Fases'
        verbose_name_plural='Fases'
        db_table = 'Fases'

        
class Timeline(models.Model):
    opcion_estado = (
        ('A', 'Activo'),
        ('I', 'Inactivo')
    )

    """ ('A', 'Aprobado'),
        ('S', 'Suspendido'),
        ('E', 'Espera'),
        ('N', 'Negado') """
    
    idtimeline = models.AutoField(primary_key=True)
    #iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    idAdoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    idpet = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200,blank=True, null=True)
    estado = models.CharField(max_length=1, choices=opcion_estado,blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    idColaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, blank = True, null = True)
    idAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, blank = True, null = True)

    fases = models.ManyToManyField(Fases, through="Timeline_fase")

    is_active = models.BooleanField(default = True)
    fecha_creacion = models.DateField(default = timezone.now)

    def all_info_user(self):
        return '{}'.format(self.idtimeline, self.idAdoptante, self.idpet, self.descripcion, self.estado, self.fecha_inicio, self.fecha_final)

    def __str__(self):
        return self.all_info_user()
    
    class Meta:
        verbose_name='timeline'
        verbose_name_plural='timelines'
        db_table = 'timeline'



class Timeline_fase(models.Model):
    opcion_estado = (
        ('A', 'Aprobado'),
        ('S', 'Suspendido'),
        ('E', 'Espera'),
        ('N', 'Negado')
    )
    fase = models.ForeignKey(Fases, on_delete=models.CASCADE, related_name = "fases_to_timeline")
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE, related_name = "timeline_to_fases")
    estado = models.CharField(max_length=1, choices=opcion_estado)
    comentarios = models.CharField(max_length=500, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default = True)
    fecha_creacion = models.DateField(default = timezone.now)

    class Meta:
        verbose_name = 'Timeline_fase'
        verbose_name_plural = 'Timeline_fase'
        db_table = 'Timeline_fase'

