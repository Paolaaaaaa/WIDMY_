from django.db import models
from manejador_de_pacientes.models import Paciente
from manejador_de_usuarios.models import Medico 

# Create your models here.
class Historia_clinica(models.Model):
    paciente = models.ForeignKey(Paciente, default=None, on_delete=models.CASCADE)
    diagnostico = models.CharField(max_length=100, default=None)
    tema = models.CharField(max_length=100, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    medicamento = models.CharField(max_length=100, default=None)
    autor_medico = models.ForeignKey(Medico, default=None,on_delete=models.SET_DEFAULT)


    def __str__(self) -> str:
        return '{}'.format(self.id_historia_clinica,self.diagnostico, self.tema, self.fecha,self.medicamento)

    #falta poner registros 