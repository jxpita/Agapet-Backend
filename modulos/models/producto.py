from django.db import models

# Create your models here.
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=75)
    marca = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
      return self.producto


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
