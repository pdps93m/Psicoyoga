from django.db import models

# Modelo de negocio de la Aplicación.

class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    estilo = models.CharField(max_length=50)
    horarios = models.CharField(max_length=50)
    
    """class Meta:
        orderimg = ["nombre"]"""
        
    def __str__(self):
        return f"{self.nombre}"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    
    """class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["nombre", "apellido"]"""""
        
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
        
class Consultas(models.Model):
    nombre = models.CharField(max_length=60)
    pregunta = models.CharField(max_length=500)
    email = models.EmailField()
    
class Ac_terapeutico(models.Model):
    nombre = models.CharField(max_length=60)
    asistSemanales = models.CharField(max_length=50)
    horario = models.IntegerField()
    email = models.EmailField()
    
class Datos_mios(models.Model):
    pass
    

