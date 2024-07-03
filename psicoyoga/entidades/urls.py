from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('estilo/', home, name="estilo"),
    path('datos_mios/', home, name="datos_mios"),
    path('consultas/', home, name="consultas"),
    path('alumno/', home, name="alumno"),
    path('ac_terapeutico', home, name="ac_terapeutico"),
    
]


