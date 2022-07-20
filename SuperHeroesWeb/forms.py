from dataclasses import fields
from django.forms import ModelForm
from .models import Personaje   

class PersonajeForm(ModelForm):
    class Meta:
        model=Personaje
        fields=['idPersonaje','nombre','descripcion','team','compagnia','foto']
