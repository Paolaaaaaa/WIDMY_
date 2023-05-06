
from ..models import Adenda, Servicio
from manejador_de_usuarios.models import Medico 
from manejador_de_usuarios.models import Enfermero 
from manejador_de_registros_de_historias_clinicas.models import Historia_clinica

def create_adenda(adenda):

    adenda_nuevo = adenda.save()
    adenda_nuevo.save()
    return adenda_nuevo

# Registro por pk
def get_adenda(pk_):
    adenda = Adenda.objects.get(pk=pk_)
    return adenda
# todo registro
def get_adendas():
    adenas = Adenda.objects.all()
    return adenas
