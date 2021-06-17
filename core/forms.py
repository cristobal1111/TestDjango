from django import forms
from django.forms import ModelForm
from .models import Vehiculo



#Creamos nuestra clase para el formulario desde la BD
class VehiculoForm(ModelForm):



    class Meta:
        model = Vehiculo
        fields =['patente','marca','modelo','categoria' ]