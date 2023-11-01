from django.db import models
from django.utils import timezone
import datetime

from django.db.models import Q

class MascotaManager(models.Manager):
    def _create_mascota(self, is_active, fecha_creacion, **extra_fields):
        mascota = self.model(
            is_active=is_active,
            fecha_creacion=fecha_creacion,
            **extra_fields
        )
        mascota.save(using=self.db)
        return mascota
    
    def create_mascota(self, **extra_fields):
        return self._create_mascota(True, timezone.now(), **extra_fields)