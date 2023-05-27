from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_usuario as lu
from .logic import logic_medico as lm
from .logic import logic_enfermero as le
from pymongo import MongoClient
from django.conf import settings
from rest_framework.parsers import JSONParser



@csrf_exempt

def usuario_view(request):

    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    usuarios = db['usuario']
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = usuarios.insert(data)
        repo ={
            "MongoObjectId":str(result),
            "Message":"Nuevo usuario en la base de datos"

        }
        client.close()
        return HttpResponse(repo,'application/json')   

@csrf_exempt
def medico_view(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    medicos = db['medico']
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = medicos.insert(data)
        repo ={
            "MongoObjectId":str(result),
            "Message":"Nuevo medico en la base de datos"

        }
        client.close()
        return HttpResponse(repo,'application/json')
    
@csrf_exempt
def get_medicos(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    medicos = db['medicos']
    if request.method == 'GET':
        result = []
        data = medicos.find({})
        for dto in data:
            jsonData = {
                "id":str(dto['_id']),
                "medico": dto['medico'],
                'threshold':dto['threshold']
            }
        
            result.append(jsonData)
        return HttpResponse(result, 'application/json')
    



@csrf_exempt
def enfermero_view(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    enfermeros = db['enfermero']
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = enfermeros.insert(data)
        repo ={
            "MongoObjectId":str(result),
            "Message":"Nuevo enfermero en la base de datos"

        }
        client.close()
        return HttpResponse(repo,'application/json')
@csrf_exempt
def get_enfermeros(request):
    client = MongoClient(settings.MONGO_CLI)
    db = client.monitoring_db
    enfermeros = db['enfermero']
    if request.method == 'GET':
        result = []
        data = enfermeros.find({})
        for dto in data:
            jsonData = {
                "id":str(dto['_id']),
                "enfermero": dto['enfermero'],
                'threshold':dto['threshold']
            }
        
            result.append(jsonData)
        return HttpResponse(result, 'application/json')