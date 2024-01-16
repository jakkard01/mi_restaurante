from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Plato

def lista_platillos(request):
    platillos = Plato.objects.all()
    return render(request, 'platillos/lista_platillos.html', {'platillos   hhh': platillos})
