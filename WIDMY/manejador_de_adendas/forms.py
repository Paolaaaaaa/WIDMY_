
from django import forms
from .models import Adenda

class AdendaForm(forms.ModelForm):
    class Meta:
        model = Adenda
        fields = [
            'historia_clinica',
            'diagnostico',
            'tema',
            'descripcion',
            'autor_medico',
            'autor_enfermero',
            'servicio'

        ]
        labels = {
            'historia_clinica': 'Historia Clinica',
            'diagnostico': 'Diagnostico',
            'tema':'Tema',
            'descripcion':'Descripcion',
            'autor_medico':'Autor Medico',
            'autor_enfermero':'Autor Enfermero',
            'servicio':'Servicio'
        }
