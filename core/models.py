from django.db import models

# Create your models here.

#Modelo para categoria


class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria


#modelO opara el cliente

class Usuario(models.Model):

    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id Usuario')
    Nombre = models.CharField(max_length=6, verbose_name='Nombre')
    Correo = models.CharField(max_length=20, verbose_name='Email')
    Contraseña = models.CharField(max_length=20,null=True, blank=True, verbose_name='Contraseña')
    def str(self):
        return self.patente
    