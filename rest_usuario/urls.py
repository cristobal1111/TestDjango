from  django.urls import path
from rest_usuario.views import lista_usuarios

urlpatterns = [
    path('lista_usuarios', lista_usuarios, name="lista_usuarios"),
]