from django.db import models
from applications.user.models import User, Administrador, Colaborador

from .managers import VacunaManager

# Create your models here.
class Vacuna(models.Model):
    vacuna_id = models.AutoField(primary_key=True)
    idAdministrador =  models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True)
    idColaborador =  models.ForeignKey(Colaborador, on_delete=models.CASCADE, null=True)
    nombre_vacuna = models.CharField(max_length=200)
    descripcion_vacuna = models.CharField(max_length=200,blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(blank = True, null = True)
    
    objects = VacunaManager()

    def info_completa(self):
        return "{}".format(self.vacuna_id,self.nombre_vacuna, self.descripcion_vacuna,self.fecha_creacion)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'vacuna'

