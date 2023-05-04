
from ..models import Adenda, Servicio
from manejador_de_usuarios.models import Medico 
from manejador_de_usuarios.models import Enfermero 
from manejador_de_registros_de_historias_clinicas.models import Historia_clinica

def create_adenda(adenda):

    if(adenda["autor_enfermero"]== "null"):
        adenda_nuevo = Adenda(
            tema = adenda['tema'],
            descripcion = adenda['descripcion'],
            autor_medico = Medico.objects.get(pk= adenda['autor_medico']),
            historia_clinica = Historia_clinica.objects.get(pk=adenda['Historia_clinica']),
            diagnostico=adenda['diagnostico'],
            servicio = Servicio.objects.get(pk= adenda['servicio']),
            autor_enfermero= None  )
        

        
    else:
        adenda_nuevo = Adenda(
            tema = adenda['tema'],
            descripcion = adenda['descripcion'],
            autor_enfermero = Enfermero.objects.get(pk= adenda['autor_enfermero']),
            historia_clinica = Historia_clinica.objects.get(pk=adenda['Historia_clinica']),
            diagnostico=adenda['diagnostico'],
            servicio = Servicio.objects.get(pk= adenda['servicio'])  )

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
