from django.db import models

# Create your models here.
class Recompensa(models.Model):
    idrecompensa = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcionInicial = models.CharField(max_length=200)
    descripcionFinal = models.CharField(max_length=200)
    precio = models.FloatField(blank=True, null=True)
    descuento = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='media/productos', blank=True, null=True)
    activo = models.BooleanField()
    puntos = models.PositiveIntegerField()

    
    def all_info_user(self):
        return '{}'.format(self.idrecompensa, self.titulo,self.descripcionInicial,
                           self.descripcionFinal,self.precio, self.descuento,self.imagen, self.activo, self.puntos)

    def __str__(self):
        return self.all_info_user()
    
    class Meta:
        verbose_name='Recompensa'
        verbose_name_plural='Recompensas'
        db_table = 'recompensa'




