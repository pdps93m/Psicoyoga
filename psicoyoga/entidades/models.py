from django.db import models

# Modelo de negocio de la Aplicación.

class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    horarios = models.CharField(max_length=50)
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    
class Consultas(models.Model):
    nombre = models.CharField(max_length=60)
    pregunta = models.CharField(max_length=500)
    email = models.EmailField()
    
class Ac_terapeutico(models.Model):
    nombre = models.CharField(max_length=60)
    pregunta = models.CharField(max_length=500)
    email = models.EmailField()
    

    

