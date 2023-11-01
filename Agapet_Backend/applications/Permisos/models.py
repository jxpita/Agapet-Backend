from django.db import models

# Create your models here.

class Permiso(models.Model):
    idPermiso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'Permiso'