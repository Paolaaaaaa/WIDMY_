from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('adenda/',views.adenda_view, name='Adenda_view'),
    path('registro/',views.registro_view, name = 'Registro_view')
]
