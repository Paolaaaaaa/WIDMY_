from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('historia_clinica/',views.historia_clinica_view, name='historia_clinica_view'),
]
