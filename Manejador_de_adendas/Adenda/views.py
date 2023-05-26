from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_adenda as la
from .logic import logic_ips as lips
from .logic import logic_servicio as ls
from django.contrib.auth.decorators import login_required
from WIDMY.auth0backend import getRole
from django.contrib import messages
from .forms import AdendaForm
from django.urls import reverse
from django.shortcuts import render,redirect
from django.conf import settings
import requests

def check_medico(data):
    medicos = requests.get(settings.PATH_MEDICO, headers={"Accept":"application/json"})
    medicoss = medicos.json()
    for med in medicoss:
        if data["autor_medico"] == med["pk"]:
            return True
    return False

def check_enfermero(data):
    enfermeros = requests.get(settings.PATH_ENFERMERO, headers={"Accept":"application/json"})
    enfermeross = enfermeros.json()
    for enf in enfermeross:
        if data["autor_enfermero"] == enf["pk"]:
            return True
    return False

@csrf_exempt
@login_required
def adenda_view(request):
    print("este es el request: ")
    role = getRole(request)
    print("este es el rol: ")
    print(role)
    if role == "Doctor" or role =="Enfermero":
        if (role =="Doctor" and check_medico(request)) or (check_enfermero(requests) and role=="Enfermero"):
            if request.method == 'POST':
                form = AdendaForm(request.POST)
                if form.is_valid():
                    adenda_dto = la.create_adenda(form)
                    adenda_dto = serializers.serialize('json',[adenda_dto])
                    print("Adenda creada")
                    messages.add_message(request, messages.SUCCESS, 'Se ha creado la adenda correctamente' )
                    return  redirect('/manejador_de_adendas/')
                else:
                    print(form.errors)
            else:
                form = AdendaForm()
            context = {
                'form':form,
            }
            return render(request, 'Adenda/AdendaCreate.html', context)
        else:

            return HttpResponse("Not existent enfermero or doctor")    

    else:
        return HttpResponse("Unauthorized User")    

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

@csrf_exempt
def get_adenda (request):
    if request.method == 'GET':
        hus = la.get_adendas()
        context = {
            'adendas_list': hus
        }
        return render(request, 'Adenda/adendas.html', context)