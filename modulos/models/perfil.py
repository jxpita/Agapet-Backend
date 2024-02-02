from django.db import models
from django.contrib.auth.admin import User
from datetime import date
from django_countries.fields import CountryField

# Create your models here.
class Perfil(models.Model):
    fechaNacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
    pais = models.CharField(max_length=25)
    ciudad = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    fotoPerfil = models.ImageField(upload_to='static/img/usuarios', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=2, choices=(('C', 'Cliente'), ('CO', 'Colaborador')), default='C')
    
    def edad(self):
        hoy = date.today()
        return hoy.year - self.fechaNacimiento.year - ((hoy.month, hoy.day) < (self.fechaNacimiento.month, self.fechaNacimiento.day))

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Perfil'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'