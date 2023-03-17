from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('usuario/',views.usuario_view, name='usuario_view'),
]
