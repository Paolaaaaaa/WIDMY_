from ..models import Historia_clinica
from django.db import models
from manejador_de_pacientes.models import Paciente
from manejador_de_usuarios.models import Medico

def create_historia_clinica(hu):
    hc_nuevo = Historia_clinica(
        paciente = Paciente.objects.get(pk = hu["paciente"]),
        autor_medico = Medico.objects.get(pk = hu['autor']),
        diagnostico = hu["diagnostico"],
        tema = hu["tema"],
        medicamento = hu["medicamento"]
    )
    hc_nuevo.save()
    return hc_nuevo


#def put_registro(reg,pk_hc):
#    hu = Historia_clinica.objects.get(pk=pk_hc)
#    reg.historia_clinica    


def get_HU(pk_):
    hu = Historia_clinica.objects.get(pk=pk_)
    return hu
# todo registro
def get_HUs():
    hus = Historia_clinica.objects.all()
    return hus