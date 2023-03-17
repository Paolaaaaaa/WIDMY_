from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('paciente',views.paciente_view, name='paciente_view'),
]
