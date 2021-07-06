from django.urls import path
from django.urls.resolvers import URLPattern
from .views import form_del_vehiculo, home,atendedor,caja,categoria,Contacto,ea,googlemap,iniciarSesion,neumaticos,nosotros,noticiass,trabajo1,trabajo2,trabajo3,trabajo4,registro,suspension,listar,form_vehiculo, form_mod_vehiculo, form_del_vehiculo





urlpatterns = [
    path('', home, name='home'),
    path('atendedor', atendedor, name='atendedor'),
    path('caja', caja, name='caja'),
    path('categoria', categoria, name='categoria'),
    path('Contacto', Contacto, name='Contacto'),
    path('ea', ea, name='ea'),
    path('googlemap', googlemap, name='googlemap'),
    path('iniciarSesion', iniciarSesion, name='iniciarSesion'),
    path('neumaticos', neumaticos, name='neumaticos'),
    path('nosotros', nosotros, name='nosotros'),
    path('noticiass', noticiass, name='noticiass'),
    path('trabajo1', trabajo1, name='trabajo1'),
    path('trabajo2', trabajo2, name='trabajo2'),
    path('trabajo3', trabajo3, name='trabajo3'),
    path('trabajo4', trabajo4, name='trabajo4'),
    path('registro', registro, name='registro'),
    path('suspension', suspension, name='suspension'),
    path('listar', listar, name='listar'),
    path('form-vehiculo', form_vehiculo, name='form_vehiculo'),
    path('form-mod-vehiculo/<id>', form_mod_vehiculo, name='form_mod_vehiculo'),
    path('form-del-vehiculo/<id>', form_del_vehiculo, name='form_del_vehiculo')
]