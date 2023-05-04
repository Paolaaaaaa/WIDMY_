from django.db import models

from ..models import Servicio,Ips
from manejador_de_usuarios.models import Medico



def create_ips(ips):
    ips_nueva = Ips.objects.create(
        nombre=ips['nombre'],
        nit = ips['nit']
    )
    ips_nueva.save()
    return ips_nueva

# Registro por pk
def get_ips(pk_):
    ips_ = Ips.objects.get(pk=pk_)
    return ips_
# todo registro
def get_ipss():
    ipss = Ips.objects.all()
    return ipss
