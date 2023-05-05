
from django import forms
from .models import Adenda

class AdendaForm(forms.ModelForm):
    class Meta:
        model = Adenda
        fields = [
            'diagnostico',
            'tema',
            'descripcion'

        ]
        labels = {
            'diagnostico': 'Diagnostico',
            'tema':'Tema',
            'descripcion':'Descripcion'
        }
