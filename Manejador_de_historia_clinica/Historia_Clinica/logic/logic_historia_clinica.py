from ..models import Historia_clinica
from django.db import models








def create_historia_clinica(hu):
    hc_nuevo = Historia_clinica(
        paciente =  hu["paciente"],
        autor_medico = hu['autor_medico'],
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