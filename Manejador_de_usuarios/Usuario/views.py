from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_usuario as lu
from .logic import logic_medico as lm
from .logic import logic_enfermero as le


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
    
@csrf_exempt
def get_medicos(request):
    if request.method == 'GET':
        medicos = lm.get_medicos()
        medicoss = serializers.serialize('json', medicos)
        return HttpResponse(medicoss, 'application/json')
    



@csrf_exempt
def enfermero_view(request):
    if request.method == 'POST':
        enfermero_dto = le.create_enfermero(json.loads(request.body))
        enfermero = serializers.serialize('json',[enfermero_dto])
        return HttpResponse(enfermero,'application/json')  
    
@csrf_exempt
def get_enfermeros(request):
    if request.method == 'GET':
        enfermeros = le.get_enfermeros()
        enfermeros = serializers.serialize('json', enfermeros)
        return HttpResponse(enfermeros, 'application/json')