
from ..models import Adenda, Servicio

from django.core.signing import Signer
from django.core.signing import dumps, loads, SignatureExpired, BadSignature
import json

def create_adenda(adenda):
    adenda_nuevo = adenda.save()
    adenda_nuevo.save()
    print(adenda_nuevo.diagnostico)
    return adenda_nuevo

# Registro por pk
def get_adenda(pk_):
    adenda = Adenda.objects.get(pk=pk_)
    return adenda
# todo registro
def get_adendas():
    adendas = Adenda.objects.all()
    return adendas
