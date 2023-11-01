from django.utils import timezone
import datetime

from django.db import models

from django.contrib.auth.models import BaseUserManager
from django.db.models import Q

 
class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, email, password, user_type, is_staff, is_superuser, last_login, is_active, date_joined, **extra_fields):
        if email is None:
            raise TypeError('Users should have a Email')
        user = self.model(
            email=self.normalize_email(email),
            user_type=user_type,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=last_login,
            is_active = is_active,
            date_joined=date_joined,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user_clb(self, email, password=None, **extra_fields):
        return self._create_user(email, password, 'CLB', False, False, timezone.now(), True, timezone.now(), **extra_fields)
        
    def create_user_adp(self, email, password=None, **extra_fields):
        return self._create_user(email, password, 'ADP', False, False, timezone.now(), True, timezone.now(), **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, 'ADM', True, True, timezone.now(), True, timezone.now(), **extra_fields)

    def listar_usuarios(self):
        return self.all()


    def buscar_usuarios(self, kuser):
        resultado = self.filter(
            Q(name__icontains=kuser) | Q(lastname__icontains=kuser) 
        )
        return resultado

    def buscar_correo(self, kuser):
        resultado = self.filter(
            Q(email=kuser) 
        )
        return resultado
    

class AdoptanteManager(models.Manager):

    def obtener_mes(self, kmonth, kyear):
        resultado = self.filter(
            Q(fecha_creacion__icontains="-"+str(kmonth)+"-") | Q(fecha_creacion__icontains="-0"+str(kmonth)+"-") & Q(fecha_creacion__icontains=kyear)
        )
        return resultado
    


