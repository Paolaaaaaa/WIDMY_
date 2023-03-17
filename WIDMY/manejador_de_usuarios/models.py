from django.db import models

# Create your models here.


class Usuario(models.Model):
    id_usuario = models.BigIntegerField()
    def __str__(self) -> str:
        return self.id_usuario


class Medico (models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.usuario
    

class Enfermero (models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.usuario