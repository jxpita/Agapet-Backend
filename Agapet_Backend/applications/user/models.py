from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
#managers
from .managers import UserManager, AdoptanteManager
from applications.Permisos.models import Permiso
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    USER_TYPE_CHOICES = (
        ('ADM','Administrador'),
        ('CLB','Colaborador'),
        ('ADP','Adoptante'),
    )
    iduser= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=100,unique=True, error_messages = {'unique':"Este correo ya se encuentra registrado."})
    direction = models.CharField(max_length=200,  blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    age = models.PositiveIntegerField( blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    username = None
    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES, blank=True)
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def all_info_user(self):
        return '{}'.format(self.iduser, self.name, self.lastname, self.email,self.direction,self.phone,self.age)

    def __str__(self):
        return self.all_info_user()
    
    def get_short_name(self):
        return self.name
    
    def get_full_name(self):
        return self.name + ' ' + self.lastname
    
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
        db_table = 'user'


class Adoptante(models.Model):
    idAdoptante = models.AutoField(primary_key=True)
    points = models.PositiveIntegerField( blank=True, null=True)
    imagen64 = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    fecha_creacion = models.DateField(auto_now=True)

    objects = AdoptanteManager()
    def info_completa(self):
        return "{}".format(self.idAdoptante,self.points)

    def __str__(self):
        return self.info_completa()
    class Meta:
        db_table = 'Adoptante'


class Administrador(models.Model):
    idAdministrador =  models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Administrador'
        db_table = 'Administrador'

    def __str__(self):
        return "{}".format(self.idAdministrador)


class Colaborador(models.Model):
    idColaborador = models.AutoField(primary_key=True)
    permisos = models.ManyToManyField(Permiso, through="Recibe_Permiso")
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    class Meta:
        db_table = 'Colaborador'

    

class Recibe_Permiso(models.Model):
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE, related_name="permiso_to_colaborador")
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name="colaborador_to_permiso")
    date_received = models.DateField()
    #valor de true o false del permiso, si lo tiene el usuario o no
    estado_permiso = models.BooleanField()

    class Meta:
        db_table = 'Recibe_Permiso'



