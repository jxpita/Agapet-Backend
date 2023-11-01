from django.db import models
from applications.user.models import Adoptante, Colaborador, Administrador, User


# Create your models here.
class Curso(models.Model):
    idcurso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    minutos = models.PositiveIntegerField()
    puntos = models.PositiveIntegerField()
    intentos = models.PositiveIntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    porcentaje = models.PositiveIntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='media/cursos', blank=True, null=True)
    
    adoptante = models.ManyToManyField(Adoptante, through = "Curso_Realizado")

    idColaborador = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.CASCADE)
    idAdministrador = models.ForeignKey(Administrador, blank=True, null=True, on_delete=models.CASCADE)

    idtema = models.ForeignKey('Tema_Curso', on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=True)

    def info_completa(self):
        return "{}".format(self.idcurso,self.titulo,self.descripcion, self.url ,self.minutos, self.puntos, self.intentos,self.fecha, self.porcentaje, self.imagen)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'curso'

class Curso_Realizado(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    date_obtained = models.DateField()
    puntos = models.PositiveIntegerField()
    is_active =  models.BooleanField(default=True)

    class Meta:
        db_table = 'Curso_Realizado'

class Tema_Curso(models.Model):
    idtema = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500, blank = True, null = True)
    idColaborador = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.CASCADE)
    idAdministrador = models.ForeignKey(Administrador, blank=True, null=True, on_delete=models.CASCADE)    
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=True)

    def info_completa(self):
        return "{}".format(self.idtema,self.tema,self.descripcion, self.descripcion)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'tema_curso'

class Formulario_Curso(models.Model):
    idFormularioCurso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    calificacion_maxima = models.PositiveIntegerField()
    formularioAdoptante = models.ManyToManyField(Adoptante, through="Formulario_Adoptante")

    def __str__(self):
        return "{}".format(self.titulo)
    
    class Meta:
        db_table = 'Formulario_Curso'

class Formulario_Adoptante(models.Model):
    idFormularioAdoptante = models.AutoField(primary_key=True)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    formularioCurso = models.ForeignKey(Formulario_Curso, on_delete=models.CASCADE)
    date_started = models.DateField()
    date_finished = models.DateField(blank=True, null=True)
    calificacion_obtenida = models.PositiveIntegerField()

    class Meta:
        db_table = 'Formulario_Adoptante'


class Pregunta(models.Model):
    idpregunta = models.AutoField(primary_key=True)
    idFormularioCurso = models.ForeignKey('Formulario_Curso', on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=200)
    puntos = models.PositiveIntegerField()
    
    def info_completa(self):
        return "{}".format(self.idpregunta,self.idFormularioCurso,self.pregunta, self.puntos)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'pregunta'

#opciones
class Respuesta(models.Model):
    idrespuesta = models.AutoField(primary_key=True)
    idpregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200)
    correcta = models.BooleanField()
    puntos = models.PositiveIntegerField()

    
    def info_completa(self):
        return "{}".format(self.idrespuesta,self.idpregunta,self.respuesta, self.correcta)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'respuesta'

class Respuesta_Seleccionada(models.Model):
    idrespuestaSeleccionada = models.AutoField(primary_key=True)
    idFormularioAdoptante = models.ForeignKey('Formulario_Adoptante', on_delete=models.CASCADE)
    idpregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    idAdoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    idrespuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)
    puntaje_obtenido = models.PositiveIntegerField()

    class Meta:
        db_table = 'Respuesta_Seleccionada'
