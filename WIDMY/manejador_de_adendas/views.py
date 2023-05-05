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
from django.shortcuts import render


@login_required
@csrf_exempt
def adenda_view(request):
    role = getRole(request)
    if role == "Doctor" or role =="Enfermero":
        if request.method == 'POST':
            form = AdendaForm(request.POST)
            if form.is_valid():
                la.create_adenda(form)
                messages.add_message(request, messages.SUCCES, 'Se ha creado la adenda correctamente' )
                return HttpResponse(reverse('adendaCreate')) 
            else:
                print(form.errors)
        else:
            form = AdendaForm()
        context = {
            'form':form,
        }
        return render(request, 'Adenda/AdendaCreate.html', context)
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
