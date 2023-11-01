from django.db import models
from applications.user.models import Administrador, Colaborador

# Create your models here.
""" class Tema(models.Model):
    temaid = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=50)
    idColaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    idAdministrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    def info_completa(self):
        return "{}".format(self.temaid,self.tema)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'tema' """


class Faq(models.Model):
    faqid = models.AutoField(primary_key=True)
    #temaid = models.ForeignKey('Tema', on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=100, blank=True, null=True )
    respuesta = models.CharField(max_length=100, blank=True, null=True)
    idColaborador = models.ForeignKey(Colaborador,blank = True, null=True, on_delete=models.CASCADE)
    idAdministrador = models.ForeignKey(Administrador, blank = True, null=True, on_delete=models.CASCADE)

    fecha_creacion = models.DateField(auto_now=True)
    is_active = models.BooleanField(default = True)

    def info_completa(self):
        return "{}".format(self.faqid,self.temaid, self.pregunta, self.respuesta)

    def __str__(self):
        return self.info_completa()
    
    class Meta:
        db_table = 'faq'