from django.db import models
from manejador_de_pacientes.models import Paciente
from manejador_de_usuarios.models import Medico 
from manejador_de_adendas.models import Registro

# Create your models here.
class Historia_clinica(models.Model):
    id_historia_clinica=models.BigIntegerField()
    paciente = models.ForeignKey(Paciente, default=None, on_delete=models.CASCADE)
    autor = models.ForeignKey(Medico, default=None, on_delete=models.CASCADE)
    registros = models.ForeignKey(Registro, default=None, on_delete=models.CASCADE, null=True)
    diagnostico = models.CharField(max_length=100, default=None)
    tema = models.CharField(max_length=100, default=None)
    fecha = models.CharField(max_length=100,default=None)
    medicamento = models.CharField(max_length=100, default=None)
    #falta poner registros 