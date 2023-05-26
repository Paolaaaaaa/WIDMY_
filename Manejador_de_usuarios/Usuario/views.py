from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_usuario as lu
from .logic import logic_medico as lm


@csrf_exempt

def usuario_view(request):
    if request.method == 'POST':
        usuario_dto = lu.create_usuario(json.loads(request.body))
        usuario = serializers.serialize('json',[usuario_dto])
        return HttpResponse(usuario,'application/json')   

@csrf_exempt
def medico_view(request):
    if request.method == 'POST':
        medico_dto = lm.create_medico(json.loads(request.body))
        medico = serializers.serialize('json',[medico_dto])
        return HttpResponse(medico,'application/json')  
    