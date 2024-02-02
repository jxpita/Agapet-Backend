from django.db import models

# Create your models here.
class TipoServicio(models.Model):
    # Fields
    idTipoServicio = models.AutoField(primary_key=True)
    tipoServicio = models.CharField(max_length = 25)
    categoria = models.CharField(max_length = 15, choices=(('veterinario', 'Veterinario'), ('aseo', 'Aseo')))
    descripcion = models.CharField(max_length = 150, blank = True, null = True)

    def __str__(self):
      return self.tipoServicio


    class Meta:
        verbose_name = 'TipoServicio'
        verbose_name_plural = 'TiposServicio'
        db_table = 'TipoServicio'
