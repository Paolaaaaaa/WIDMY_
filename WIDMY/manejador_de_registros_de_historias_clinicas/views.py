from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_historia_clinica as lhc
from manejador_de_adendas.logic import logic_registro as lr


@csrf_exempt

def historia_clinica_view(request):
    if request.method == 'POST':
        hc_dto = lhc.create_historia_clinica(json.loads(request.body))
        hc = serializers.serialize('json',[hc_dto])
        return HttpResponse(hc,'application/json')    
    
@csrf_exempt
#GET ONE
def historia_clinica_get_one(request, pk):
    if request.method == 'GET':
        hc = lhc.get_HU(pk)
        hc = serializers.serialize('json',[hc,])
        return HttpResponse(hc,'application/json')

@csrf_exempt

def historia_clinica_registro_create(request, pk):
    if request.method =='POST':
        reg_dto = lr.create_registro(json.loads(request.body))
        hu_ret = lr.put_registro(reg_dto,pk)
        hu_ret =serializers.serialize('json',[hu_ret])
        return HttpResponse(hu_ret,'application/json')


