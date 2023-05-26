from django.db import models


# Create your models here.
class Historia_clinica(models.Model):
    paciente = models.IntegerField(null=False, default=None)
    diagnostico = models.CharField(max_length=100, default=None)
    tema = models.CharField(max_length=100, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    medicamento = models.CharField(max_length=100, default=None)
    autor_medico = models.IntegerField(null=False, default=None)

    def __str__(self) -> str:
        return '{}'.format(self.diagnostico, self.tema, self.fecha,self.medicamento)

    #falta poner registros