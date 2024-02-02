from django.db import models

# Create your models here.
class TipoEvento(models.Model):
    idTipoEvento = models.AutoField(primary_key=True)
    tipoEvento = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
      return self.tipoEvento

    class Meta:
        verbose_name = 'TipoEvento'
        verbose_name_plural = 'TiposEvento'
        db_table = 'TipoEvento'
