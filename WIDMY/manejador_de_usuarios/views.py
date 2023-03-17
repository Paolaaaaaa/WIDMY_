from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_usuario as lu


@csrf_exempt

def usuario_view(request):
    if request.method == 'POST':
        usuario_dto = lu.create_usuario(json.loads(request.body))
        usuario = serializers.serialize('json',[usuario_dto])
        return HttpResponse(usuario,'application/json')    
    