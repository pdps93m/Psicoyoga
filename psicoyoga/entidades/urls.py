from django.urls import path, include
from .views import *
from entidades import views

urlpatterns = [
    path('', home, name="home"),
    path('estilo/', views.estilo, name="estilo"),
    path('datos_mios/', views.datos_mios, name="datos_mios"),
    path('consultas/', views.consultas, name="consultas"),
    path('alumno/', views.alumno, name="alumno"),
    path('ac_terapeutico', views.ac_terapeutico, name="ac_terapeutico"),
    
    
    #_____ Formularios
    path('estiloForm', estiloForm, name="estiloform"),
    path('alumnoForm', alumnoForm, name="alumnoform"),
    path('ac_terapForm', ac_terapForm, name="ac_terapForm"),
    

]


