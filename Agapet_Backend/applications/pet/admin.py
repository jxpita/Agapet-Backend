from django.contrib import admin
from .models import Animal, Mascota, Vacunado

# Register your models here.
admin.site.register(Animal)
admin.site.register(Mascota)
admin.site.register(Vacunado)