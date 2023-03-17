from django.db import models
from manejador_de_personal_medico.models import Personal_medico
from manejador_de_registros_de_historias_clinicas import Historia_clinica
# Create your models here.

class Registro(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    tema =models.CharField(_(""), max_length=50)
    diagnostico=models.CharField(max_length=50)
    historia_clinica = models.ForeignKey(Historia_clinica, default=None, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}'.format(self.fecha,self.tema, self.diagnostico, self.historia_clinica)


class Adenda(models.Model):
    fecha = models.DateField(auto_now_add=True)
    tema= models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    autor = models.ForeignKey(Personal_medico, default=None)
    registro= models.ForeignKey(Registro, default=None, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}'.format(self.fecha,self.tema, self.descripcion, self.autor, self.registro)

