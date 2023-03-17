from ..models import Usuario
from manejador_de_pacientes.models import Paciente


def create_usuario(usuario):
    usuario_nuevo = Usuario(
        id_usuario= Paciente.objects.get(pk=usuario["id_usuario"])
        
    )
    usuario_nuevo.save()
    return usuario_nuevo




def get_paciente(pk_):
    usuario = Usuario.objects.get(pk=pk_)
    return usuario
# todo registro
def get_Pacientes():
    usuarios = Usuario.objects.all()
    return usuarios