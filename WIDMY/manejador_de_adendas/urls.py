from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('adenda/',views.adenda_view, name='Adenda_view'),
    path('ips/', views.ips_view, name='ips_view'),
    path ('service/', views.servicio_views, name='servicio_view')
]
