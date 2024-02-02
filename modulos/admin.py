from django.contrib import admin
from modulos.models.perfil import Perfil
from modulos.models.alimento import Alimento
from modulos.models.producto import Producto
from modulos.models.raza import Raza
from modulos.models.notificacion import Notificacion
from modulos.models.tiposervicio import TipoServicio
from modulos.models.servicio import Servicio
from modulos.models.tipoevento import TipoEvento
from modulos.models.evento import Evento
from modulos.models.eventointeres import EventoInteres
from modulos.models.tipoanimal import TipoAnimal
from modulos.models.animal import Animal

# Register your models here.
admin.site.register(Perfil)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechaNacimiento', 'genero', 'pais', 'ciudad', 'direccion', 'fotoPerfil', 'user')
    search_fields = ('id', 'fechaNacimiento', 'genero', 'pais', 'ciudad', 'direccion', 'fotoPerfil', 'user')
    list_filter = ('id', 'fechaNacimiento', 'genero', 'pais', 'ciudad', 'direccion', 'fotoPerfil', 'user')

    
admin.site.register(Alimento)
admin.site.register(Producto)
admin.site.register(Raza)
admin.site.register(Notificacion)
admin.site.register(TipoServicio)
admin.site.register(Servicio)
admin.site.register(TipoEvento)
admin.site.register(Evento)
admin.site.register(EventoInteres)
admin.site.register(TipoAnimal)
admin.site.register(Animal)
