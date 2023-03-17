from..models import Registro
from manejador_de_registros_de_historias_clinicas.models import Historia_clinica
#crear un registro

def create_registro(registro):
    reg_nuevo = Registro(
        fecha = registro['fecha'],
        tema = registro['tema'],
        diagnostico = registro['diagnostico'],
        historia_clinica = Historia_clinica.objects.get(pk= registro["historia_clinica"])

    )
    reg_nuevo.save()
    return reg_nuevo

# Registro por pk
def get_registro(pk_):
    registro = Registro.objects.get(pk=pk_)
    return registro
# todo registro
def get_registos():
    registros = Registro.objects.all()
    return registros
