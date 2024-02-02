from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Notificacion(models.Model):
    idNotificacion = models.AutoField(primary_key=True)
    usuarioANotificar = models.ForeignKey(User, on_delete=models.CASCADE)
    tipoNotificacion = models.CharField(max_length=15, choices=(('evento', 'Evento'), ('servicio', 'Servicio')))
    titulo = models.CharField(max_length=25)
    contenido = models.CharField(max_length=150)
    fechaNotificacion = models.DateTimeField(default=datetime.now())

    def __str__(self):
      return str(self.idNotificacion)


    class Meta:
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'
        db_table = 'Notificacion'
