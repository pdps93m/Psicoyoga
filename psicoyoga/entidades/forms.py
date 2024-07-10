from django import forms
    


class EstiloForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    estilo = forms.CharField(max_length=50, required=True)
    horarios = forms.CharField(max_length=50, required=True)
    
class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(required=True)
    email = forms.CharField(max_length=50, required=True)
    
class ActerapForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    asist_semanales = forms.IntegerField(required=True)
    horario = forms.CharField(max_length=50, required=True)
    email= forms.EmailField(max_length=50,required=True)
    
  