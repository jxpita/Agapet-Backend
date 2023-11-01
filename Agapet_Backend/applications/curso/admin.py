from django.contrib import admin
from .models import (
    Curso,
    Curso_Realizado, 
    Tema_Curso, 
    Formulario_Curso, 
    Formulario_Adoptante, 
    Pregunta,
    Respuesta, 
    Respuesta_Seleccionada

)

# Register your models here.
admin.site.register(Curso)
admin.site.register(Curso_Realizado)
admin.site.register(Tema_Curso)
admin.site.register(Formulario_Curso)
admin.site.register(Formulario_Adoptante)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Respuesta_Seleccionada)