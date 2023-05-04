from django.contrib import admin
from .models import Servicio,Adenda, Ips

admin.site.register(Adenda)
admin.site.register(Servicio)
admin.site.register(Ips)

# Register your models here.
