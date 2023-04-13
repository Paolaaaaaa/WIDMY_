
from ..models import Adenda
from ..models import Registro
from manejador_de_usuarios.models import Medico 
from manejador_de_usuarios.models import Enfermero 

def create_adenda(adenda):

    if(adenda["autor_enfermero"]== "null"):
        adenda_nuevo = Adenda(
            tema = adenda['tema'],
            descripcion = adenda['descripcion'],
            autor_medico = Medico.objects.get(pk= adenda['autor_medico']),
            registros = Registro.objects.get(pk= adenda["registro"]),

        )
    else:
        adenda_nuevo = Adenda(
            tema = adenda['tema'],
            descripcion = adenda['descripcion'],
            autor_enfermero = Enfermero.objects.get(pk= adenda['autor_enfermero']),
            registros = Registro.objects.get(pk= adenda["registro"]),

        )

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
