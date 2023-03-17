from django.db import models
from manejador_de_usuarios.models import Medico 
from manejador_de_usuarios.models import Enfermero 

# Create your models here.


class Adenda(models.Model):
    fecha = models.DateField(auto_now_add=True)
    tema= models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    autor_medico = models.ForeignKey(Medico, default=None,on_delete=models.SET_DEFAULT)
    autor_enfermero = models.ForeignKey(Enfermero, default=None, on_delete=models.SET_DEFAULT)


    def __str__(self) -> str:
        return '{}'.format(self.fecha,self.tema, self.descripcion, self.autor, self.registro)


class Registro(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tema =models.CharField( max_length=50)
    diagnostico=models.CharField(max_length=50)
    adenda= models.ForeignKey(Adenda, default=None, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return '{}'.format(self.fecha,self.tema, self.diagnostico, self.historia_clinica)
