from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_paciente as lp


@csrf_exempt

def paciente_view(request):
    if request.method == 'POST':
        paciente_dto = lp.create_paciente(json.loads(request.body))
        paciente = serializers.serialize('json',[paciente_dto])
        return HttpResponse(paciente,'application/json')    
    

@csrf_exempt
def get_pacientes(request):
    if request.method == 'GET':
        pacientes = lp.get_Pacientes()
        variables = serializers.serialize('json', pacientes)
        return HttpResponse(variables, 'application/json')
     
