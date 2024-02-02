from django.db import models
from modulos.models.evento import Evento
from django.contrib.auth.models import User

# Create your models here.
class EventoInteres(models.Model):
    # Fields
    idEventoInteres = models.AutoField(primary_key=True)
    tituloEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    idUsuarioInteresado = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.tituloEvento


    class Meta:
        verbose_name = 'EventoInteres'
        verbose_name_plural = 'EventosInteres'
        db_table = 'EventoInteres'
