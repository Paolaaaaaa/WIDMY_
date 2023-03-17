
from ..models import Adenda
from ..models import Registro
from manejador_de_personal_medico.models import Personal_medico


def create_registro(adenda):
    reg_nuevo = Adenda(
        fecha = adenda['fecha'],
        tema = adenda['tema'],
        descripcion = adenda['descripcion'],
        autor = Personal_medico.objects.get(pk= adenda['autor']),
        registro = Registro.objects.get(pk= adenda["registro"])

    )
    reg_nuevo.save()
    return reg_nuevo

# Registro por pk
def get_adenda(pk_):
    adenda = Adenda.objects.get(pk=pk_)
    return adenda
# todo registro
def get_adendas():
    adenas = Adenda.objects.all()
    return adenas
