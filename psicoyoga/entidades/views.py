from django.shortcuts import render
from .models import *
from entidades.static import*
from .forms import *
# Create your views here.

def home(request):
    return render(request, "entidades/index.html")

def alumno(request):
    contexto = {"alumno": Alumno.objects.all()}
    return render(request, "entidades/alumno.html", contexto)

def estilo(request):
    contexto = {"estilo": Estilo.objects.all()}
    return render(request, "entidades/estilo.html", contexto)

def consultas(request):
    contexto = {"consultas": Consultas.objects.all()}
    return render(request, "entidades/consultas.html", contexto)

def datos_mios(request):
    return render(request, "entidades/datos_mios.html")

def ac_terapeutico(request):
    contexto = {"acompañamiento_terapeutico": Ac_terapeutico.objects.all()}
    return render(request, "entidades/ac_terapeutico.html")

#_____ Formularios

def estiloForm(request):
    if request.method == "POST":
       miForm =EstiloForm(request.POST)
       if miForm.is_valid():
           nombre = miForm.cleaned_data.get("nombre")
           estilo = miForm.cleaned_data.get("estilo")
           horario = miForm.cleaned_data.get("horario")
           estilo = Estilo(nombre=nombre, estilo=estilo, horarios=horario)
           estilo.save()
           contexto = {"estilo": Estilo.objects.all()}
           return render(request, "entidades/estilo.html", contexto)
    else:
        miForm = EstiloForm()
    
    return render(request, "entidades/estiloForm.html", {"form": miForm})

def alumnoForm(request):
    if request.method == "POST":
        miForm =AlumnoForm(request.POST)
        if miForm.is_valid():
           nombre = miForm.cleaned_data.get("nombre")
           apellido = miForm.cleaned_data.get("apellido")
           email = miForm.cleaned_data.get("email")
           alumno = Alumno(nombre=nombre, apellido=apellido, email=email)
           alumno.save()
           contexto = {"alumno": Alumno.objects.all()}
           return render(request, "entidades/alumno.html", contexto) 
    else:
        miForm = AlumnoForm()
    
    return render(request, "entidades/alumnoForm.html", {"form": miForm})

def ac_terapForm(request):
    if request.method == "POST":
        miForm =ActerapForm(request.POST)
        if miForm.is_valid():
           nombre = miForm.cleaned_data.get("nombre")
           asist_semanales = miForm.cleaned_data.get("asistencias")
           horario = miForm.cleaned_data.get("horario")
           email = miForm.cleaned_data.get("email") 
           ac_terapeutico = Ac_terapeutico(nombre=nombre, asist_semanales=asist_semanales, horario=horario, email=email)
           ac_terapeutico.save()
           contexto = {"acompañamiento_terapeutico": Ac_terapeutico.objects.all()}
           return render(request, "entidades/ac_terapeutico.html")
           
    else:
        miForm = ActerapForm()
    
    return render(request, "entidades/ac_terapForm.html", {"form": miForm})