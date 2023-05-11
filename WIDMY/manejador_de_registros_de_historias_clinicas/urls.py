from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('historia_clinica/',views.historia_clinica_view, name='historia_clinica_view'),
    path('historia_clinica/<int:pk>/',views.historia_clinica_get_one, name='historia_clinica_get_one'),
    path('historias_clinicas/',views.historias_clinicas_list, name = "lista_historias_clinicas"),


]
