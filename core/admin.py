from django.contrib import admin
from .models import Categoria, CategoriaUsuario, Usuario, Vehiculo 

# Register your models here.
#Permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(CategoriaUsuario)



