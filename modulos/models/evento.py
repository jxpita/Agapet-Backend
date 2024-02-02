from django.db import models
from django.utils import timezone
from modulos.models.tipoevento import TipoEvento
from datetime import datetime, date, timedelta

class Evento(models.Model):
    # Fields
    idEvento = models.AutoField(primary_key=True)
    tituloEvento = models.CharField(max_length=75)
    tipoEvento = models.CharField(max_length=15, choices=(('adopcion', 'Adopcion'), ('campaña', 'Campaña'), ('voluntariado', 'Voluntariado')))
    lugarEvento = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fechaCreacionEvento = models.DateTimeField(default=timezone.now)
    fechaEvento = models.DateField(default=timezone.now)
    horaInicioEvento = models.TimeField(blank=True, null=True)
    horaFinEvento = models.TimeField(blank=True, null=True)
    precioEvento = models.PositiveSmallIntegerField(blank=True, null=True)
    descuento = models.PositiveSmallIntegerField(blank=True, null=True)
    imagenPromocional = models.ImageField(upload_to='static/img/eventos', blank=True, null=True)
    estado = models.CharField(max_length=15, null=True, choices=(('activado', 'Activado'), ('desactivado', 'Desactivado')))

    def str(self):
      return self.tituloEvento

    def save(self, *args, **kwargs):  # Asegúrate de incluir *args y **kwargs aquí
        if not self.horaInicioEvento:
            self.horaInicioEvento = timezone.now().time()
        if not self.horaFinEvento:
            # Convertir horaInicioEvento a datetime para sumar timedelta
            datetime_inicio = timezone.now().replace(hour=self.horaInicioEvento.hour, minute=self.horaInicioEvento.minute, second=0, microsecond=0)
            datetime_fin = datetime_inicio + timedelta(hours=1)
            self.horaFinEvento = datetime_fin.time()
        
        super(Evento, self).save(*args, **kwargs)  # Pasa *args y **kwargs al método save base

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        db_table = 'Evento'