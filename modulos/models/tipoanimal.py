from django.db import models

# Create your models here.
class TipoAnimal(models.Model):
    idTipoAnimal = models.AutoField(primary_key=True)
    tipoAnimal = models.CharField(max_length=50)

    def __str__(self):
      return self.tipoAnimal


    class Meta:
        verbose_name = 'TipoAnimal'
        verbose_name_plural = 'TiposAnimal'
        db_table = 'TipoAnimal'
