from django.utils import timezone
import datetime

from django.db import models

from django.db.models import Q

class FaseManager(models.Manager):
    def _create_fase(self, is_active, fecha_creacion, **extra_fields):
        fase = self.model(
            is_active=is_active,
            fecha_creacion=fecha_creacion,
            **extra_fields
        )
        fase.save()
        return fase
        
    def create_fase(self, **extra_fields):
        return self._create_fase(True, timezone.now(), **extra_fields)