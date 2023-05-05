from django.db import models
from manejador_de_usuarios.models import Medico 
from manejador_de_usuarios.models import Enfermero 
from manejador_de_registros_de_historias_clinicas.models import Historia_clinica

# Create your models here.

class Ips(models.Model):
     nombre = models.CharField(max_length=50)
     nit = models.BigIntegerField()

     def __str__(self) -> str:
          return '{}'.format(self.nombre, self.nit)
     
class Servicio(models.Model):
        descripcion = models.CharField(max_length=100)
        nombre = models.CharField(max_length=50)
        ips_doctor =models.ForeignKey(Medico, default=None, blank = True, on_delete = models.SET_NULL,null=True)
        ips = models.ForeignKey(Ips,default=None, blank=True, on_delete=models.CASCADE)  
        def __str__(self) -> str:
             return '{}'.format(self.descripcion,self.nombre,self.ips_doctor, self.ips)   

class Adenda(models.Model):
    historia_clinica = models.OneToOneField(Historia_clinica, default= None, on_delete=models.CASCADE, primary_key=True)
    diagnostico=models.CharField(max_length=50, default=None)
    fecha = models.DateField(auto_now_add=True)
    tema= models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)# comentarios 
    autor_medico = models.ForeignKey(Medico, default=None,on_delete=models.SET_DEFAULT, blank= True, null= True)
    autor_enfermero = models.ForeignKey(Enfermero, default=None, on_delete=models.SET_DEFAULT, blank= True,null= True)
    servicio = models.ForeignKey(Servicio, default=None, blank=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{}'.format(self.fecha,self.tema, self.descripcion, self.diagnostico)
    





