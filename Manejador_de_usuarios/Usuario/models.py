from django.db import models

# Create your models here.
"""

class Usuario(models.Model):
    id_usuario = models.BigIntegerField(default=None)

    class Meta:
        abstract= True
    def __str__(self) :
        return '{} '.format(self.pk)


class Medico (Usuario):
    profesion = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.pk
    

class Enfermero (Usuario):
    profesion = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.pk



"""