from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Usuario, Vehiculo



#Creamos nuestra clase para el formulario desde la BD
class VehiculoForm(ModelForm):



    class Meta:
        model = Vehiculo
        fields =['patente','marca','modelo','categoria' ]


#Crearemos la clase usuario
class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields =['nombre', 'email', 'contrasena']

class CustomUserCreationForm(UsuarioForm):
    pass