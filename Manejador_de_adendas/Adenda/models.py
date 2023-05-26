from django.db import models
from django_cryptography.fields import encrypt
# Create your models here.




class Ips(models.Model):
     nombre = models.CharField(max_length=50)
     nit = models.BigIntegerField()

     def __str__(self) -> str:
          return '{}'.format(self.nombre, self.nit)
     
class Servicio(models.Model):
        descripcion = models.CharField(max_length=100)
        nombre = models.CharField(max_length=50)
        ips_doctor =models.IntegerField(null=False, default=None)
        ips = models.ForeignKey(Ips,default=None, blank=True, on_delete=models.CASCADE)  
        def __str__(self) -> str:
             return '{}'.format(self.descripcion,self.nombre,self.ips_doctor, self.ips)   

class Adenda(models.Model):
    historia_clinica = models.IntegerField(null=False, default=None)
    diagnostico = encrypt(models.CharField(max_length=50, default=None))
    fecha = models.DateField(auto_now_add=True)
    tema= encrypt(models.CharField(max_length=50, default= None))
    descripcion = encrypt(models.CharField(max_length=100, default=None))# comentarios 
    autor_medico = models.IntegerField(null=False, default=None)
    autor_enfermero =models.IntegerField(null=False, default=None)
    servicio = (models.ForeignKey(Servicio, default=None, blank=True, on_delete=models.CASCADE))
    def __str__(self) -> str:
        return '{}'.format(self.tema, self.descripcion, self.diagnostico, self.autor_enfermero, self.autor_medico, self.servicio, self.historia_clinica)
    



