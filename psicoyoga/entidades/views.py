from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, "entidades/index.html")

def alumno(request):
    return render(request, "entidades/index.html")

def estilo(request):
    contexto = {"estilo": Estilo.objets.all()}
    return render(request, "entidades/index.html", contexto)

def consultas(request):
    return render(request, "entidades/index.html")

def datos_mios(request):
    return render(request, "entidades/index.html")

def ac_terapeutico(request):
    return render(request, "entidades/index.html")
