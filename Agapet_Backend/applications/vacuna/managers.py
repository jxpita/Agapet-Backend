from django.utils import timezone
import datetime

from django.db import models

from django.db.models import Q

class VacunaManager(models.Manager):
    def _create_vacuna(self, is_active, fecha_creacion, **extra_fields):
        mascota = self.model(
            is_active=is_active,
            fecha_creacion=fecha_creacion,
            **extra_fields
        )
        mascota.save(using=self.db)
        return mascota

    def create_vacuna(self, **extra_fields):
        return self._create_vacuna(True, timezone.now(), **extra_fields)
    