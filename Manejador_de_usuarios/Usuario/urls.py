from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('usuario/',views.usuario_view, name='usuario_view'),
    path('medico/', views.medico_view, name= 'medico_view'),
    path('medico/list/',views.get_medicos, name='get_medicos'),
    path('enfermero/', views.enfermero_view, name= 'create_enfermero'),
    path ('enfermero/list', views.get_enfermeros, name = 'get_enfermeros'),
]
