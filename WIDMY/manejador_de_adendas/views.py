from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_adenda as la
from .logic import logic_registro as lr

@csrf_exempt

def adenda_view(request):
    if request.method == 'POST':
        adenda_dto = la.create_adenda(json.loads(request.body.decode('utf-8')))
        adenda = serializers.serialize('json',[adenda_dto])
        return HttpResponse(adenda,'application/json')    
    
@csrf_exempt

def registro_view(request):
    if request.method =='POST':
        registro_dto = lr.create_registro(json.loads(request.body))
        registro = serializers.serialize('json', [registro_dto])
        return HttpResponse(registro,'application/json')    

# Create your views here.
