from django.contrib import admin
from .models import User, Adoptante, Administrador, Colaborador, Recibe_Permiso

# Register your models here.
admin.site.register(User)
admin.site.register(Adoptante)
admin.site.register(Administrador)
admin.site.register(Colaborador)
admin.site.register(Recibe_Permiso)