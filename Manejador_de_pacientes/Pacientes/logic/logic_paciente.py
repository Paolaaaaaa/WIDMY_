

from ..models import Paciente


def create_paciente(paciente):
    paciente_nuevo = Paciente(
        id_paciente= paciente['id_paciente']
        
    )
    paciente_nuevo.save()
    return paciente_nuevo




def get_paciente(pk_):
    paciente = Paciente.objects.get(pk=pk_)
    return paciente
# todo registro
def get_Pacientes():
    pacientes = Paciente.objects.all()
    return pacientes