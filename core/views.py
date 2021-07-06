from core.forms import VehiculoForm
from django.shortcuts import render, redirect
from .models import Vehiculo

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def atendedor(request):
    return render(request, 'core/atendedor.html')

def caja(request):
    return render(request, 'core/caja.html')

def categoria(request):
    return render(request, 'core/categoria.html')

def Contacto(request):
    return render(request, 'core/Contacto.html')

def ea(request):
    return render(request, 'core/ea.html')

def googlemap(request):
    return render (request, 'core/googlemap.html')

def iniciarSesion(request):
    return render(request, 'core/iniciarSesion.html')

def neumaticos(request):
    return render(request, 'core/neumaticos.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def noticiass(request):
    return render(request, 'core/noticiass.html')

def trabajo1(request):
    return render(request, 'core/trabajo1.html')

def trabajo2(request):
    return render(request, 'core/trabajo2.html')

def trabajo3(request):
    return render(request, 'core/trabajo3.html')

def trabajo4(request):
    return render(request, 'core/trabajo4.html')

def registro(request):
    return render(request, 'core/registro.html')

def suspension(request):
    return render(request, 'core/suspension.html')

def listar(request):

    vehiculos= Vehiculo.objects.all()

    datos = {
        'vehiculos':vehiculos
    }
    return render(request, 'core/listar.html',datos)

def form_vehiculo(request):
    datos={
        'form' : VehiculoForm()
    }

    if request.method=='POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_vehiculo.html', datos)

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos= {
        'form': VehiculoForm(instance=vehiculo)
    }

    if request.method=='POST':
        formulario = VehiculoForm(data=request.POST,instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/form_mod_vehiculo.html', datos)

def form_del_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to='home')
    