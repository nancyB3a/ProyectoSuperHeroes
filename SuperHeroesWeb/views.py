from django.shortcuts import redirect, render
from .models import Personaje
from .forms import PersonajeForm

from SuperHeroesWeb.models import Personaje

# Create your views here.
def index(request):
    persMarvel=Personaje.objects.filter(compagnia=1)
    persDC=Personaje.objects.filter(compagnia=2)
    datos={
        'pMarvel':persMarvel,
        'pDC':persDC
    }
    return render(request,'SuperHeroesWeb/index.html', datos)

def listaPersonajes(request):
    personajes=Personaje.objects.all()
    datos={
        'personajes':personajes
    }
    return render(request,'SuperHeroesWeb/listaPersonajes.html', datos)

def form_personaje(request):
    datos={
        'form':PersonajeForm
    }
    if request.method=='POST':
        formulario=PersonajeForm(request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardado Correctamente"
    return render(request, 'SuperHeroesWeb/form_personaje.html',datos)

def form_mod_personaje(request,id):
    personaje=Personaje.objects.get(idPersonaje=id)
    datos={
        'form': PersonajeForm(instance=personaje)
    }
    if request.method=='POST':
        formulario=PersonajeForm(request.POST, instance=personaje)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado Correctamente"
    return render(request, 'SuperHeroesWeb/form_mod_personaje.html',datos)

def form_del_personaje(request,id):
    personaje=Personaje.objects.get(idPersonaje=id)
    personaje.delete()
    return redirect(to='listaPersonajes')