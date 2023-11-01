from django.db import models
from applications.user.models import User, Colaborador, Administrador, Adoptante
from django.core.validators import MaxValueValidator, MinValueValidator

from applications.vacuna.models import Vacuna
from .managers import MascotaManager

class Animal(models.Model):
    idanimal = models.AutoField(primary_key=True)
    tipoanimal = models.CharField(max_length=50)

    def info_completa(self):
        return "{}".format(self.idanimal,self.tipoanimal)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'animal'


# Create your models here.
class Mascota(models.Model):

    opcion_genero = (
        ('M', 'Macho'),
        ('H', 'Hembra'),
    )

    opcion_estado = (
        ('S', 'Disponible'),
        ('N', 'No Disponible'), 
    )

    opcion_adoptado = (
        ('AD', 'Adoptado'),
        ('NA', 'No Adoptado'),
    )

    
    idpet = models.AutoField(primary_key=True)
    #iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE, null=True, related_name="adoptante_mascota")
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null=True)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=opcion_genero)
    estado = models.CharField(max_length=1, choices=opcion_estado) #estado disponible o no
    adopted = models.CharField(max_length=2, choices=opcion_adoptado, default=opcion_adoptado[1][0])
    #para adopción adoptado o no
    #ENVIAR LISTA DE MASCOTAS FILTRADAS POR DOS ESTADOS
    descripcion = models.CharField(max_length=200)
    image64 = models.TextField(blank = True, null = True)
    edad = models.FloatField()
    peso = models.FloatField()
    
    comida = models.CharField(max_length=50)
    deportivo = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator (1)])
    jugueton = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator (1)])
    sociable = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator (1)])
    miedoso = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator (1)])
    
    # Esterilizado
    esterilizado = models.CharField(max_length=1)
    fecha_esterilizado = models.DateField(blank=True, null=True)
    lugar_esterilizado = models.CharField(max_length=100,blank=True, null=True)
    descripcion_esterilizado = models.CharField(max_length=200,blank=True, null=True)
    
    # Desparacitado
    desparacitado = models.CharField(max_length=1)
    fecha_desparacitado = models.DateField(blank=True, null=True)
    lugar_desparacitado = models.CharField(max_length=100,blank=True, null=True)
    descripcion_desparacitado = models.CharField(max_length=200,blank=True, null=True)

    vacunas = models.ManyToManyField(Vacuna, through="Vacunado")

    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateField(blank=True, null=True)

    objects = MascotaManager()

    def all_info_user(self):
        return '{}'.format(self.idpet,self.adoptante, self.animal,self.nombre,self.genero,self.estado,self.descripcion,
        self.edad,self.peso, self.comida, self.deportivo, self.jugueton, self.sociable, self.miedoso, self.esterilizado,
        self.fecha_esterilizado, self.lugar_esterilizado, self.descripcion_esterilizado, self.desparacitado,
        self.fecha_desparacitado, self.lugar_desparacitado, self.descripcion_desparacitado)

    def __str__(self):
        return self.all_info_user()
    
    class Meta:
        verbose_name='Mascota'
        verbose_name_plural='Mascotas'
        db_table = 'mascota'


class Vacunado(models.Model):
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE, related_name="vacunado_to_mascota")
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="mascota_to_vacuna")
    descripcion_vacunacion = models.CharField(max_length=500, blank=True, null=True)
    imagen64 = models.TextField(blank=True, null=True)
    lugar_vacunacion = models.CharField(max_length=100,blank=True, null=True)
    fecha_vacunacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.vacuna, self.mascota)

    class Meta:
        db_table = 'Vacunado'

