from django.db import models

from ..models import Servicio,Ips



def create_servicio(servicio):
    servicio_nuevo = Servicio.objects.create(
        descripcion = servicio['descripcion'],
        nombre = servicio['nombre'],
        #ips_doctor = Medico.objects.get(pk=servicio['ips_doctor']),
        ips = Ips.objects.get(pk= servicio['ips'])

    )
    servicio_nuevo.save()
    return servicio_nuevo
 

# Registro por pk
def get_servicio(pk_):
    serv = Servicio.objects.get(pk=pk_)
    return serv
# todo registro
def get_adendas():
    servicio_ = Servicio.objects.all()
    return servicio_
