from django.db import models

class Personal_medico(models.Model):
    tipo = models.CharField(max_length=10)
    profesion = models.CharField(max_length=20)