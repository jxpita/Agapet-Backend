from django.db import models
from modulos.models.tipoanimal import TipoAnimal

# Create your models here.
class Raza(models.Model):
    idRaza = models.AutoField(primary_key=True)
    raza = models.CharField(max_length=50)

    # Foreign Keys
    idTipoAnimal = models.ForeignKey(TipoAnimal, blank = True, null=True, on_delete=models.CASCADE)

    def __str__(self):
      return self.raza


    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'
        db_table = 'Raza'
