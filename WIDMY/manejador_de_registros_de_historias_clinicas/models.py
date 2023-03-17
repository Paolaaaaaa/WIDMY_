from django.db import models
from manejador_de_pacientes import Paciente

# Create your models here.
class Historia_clinica(models.Model):
    id_historia_clinica=models.BigIntegerField()
    paciente = models.ForeignKey(Paciente, default=None, on_delete=models.CASCADE)