from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_paciente = models.BigIntegerField()


    def __str__(self) -> str:
        return self.id_paciente