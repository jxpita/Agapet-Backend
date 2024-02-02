from django.db import models
from modulos.models.tipoanimal import TipoAnimal

# Create your models here.
class Alimento(models.Model):
    idAlimento = models.AutoField(primary_key=True)
    alimento = models.CharField(max_length=50)
    marca = models.CharField(max_length=15, blank=True, null=True)

    # Foreign Keys
    idTipoAnimal = models.ForeignKey(TipoAnimal, blank = True, null=True, on_delete=models.CASCADE)

    def __str__(self):
      return self.alimento


    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        db_table = 'Alimento'
