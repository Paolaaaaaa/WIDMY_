from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_adenda as la
from .logic import logic_ips as lips
from .logic import logic_servicio as ls

@csrf_exempt

def adenda_view(request):
    if request.method == 'POST':
        adenda_dto = la.create_adenda(json.loads(request.body.decode('utf-8')))
        adenda = serializers.serialize('json',[adenda_dto])
        return HttpResponse(adenda,'application/json')    
    

# Create your views here
@csrf_exempt
def ips_view(request):
    if request.method == 'POST':
        ips_dto = lips.create_ips(json.loads(request.body.decode('utf-8')))
        ips_dto = serializers.serialize('json',[ips_dto])
        return HttpResponse(ips_dto,'application/json')
    
@csrf_exempt
def servicio_views (request):
    if request.method == 'POST':
        service_dto = ls.create_servicio(json.loads(request.body.decode('utf-8')))
        service_dto = serializers.serialize('json',[service_dto])
        return HttpResponse (service_dto, 'application/json')
