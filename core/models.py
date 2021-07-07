from django.db import models
# Create your models here.

#Modelo para categoria


class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

#Modelo para el Vehiculo

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6,primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca Vehiculo')
    modelo = models.CharField(max_length=20,null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def str(self):
        return self.patente


#modelO opara el cliente

class Usuario(models.Model):

    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id Usuario')
    Nombre = models.CharField(max_length=6, verbose_name='Nombre')
    Correo = models.CharField(max_length=20, verbose_name='Email')
    Contraseña = models.CharField(max_length=20,null=True, blank=True, verbose_name='Contraseña')
    
    def str(self):
        return self.patente
    
 
    #Categoria para el usuario

class CategoriaUsuario(models.Model):
    iddCategoria = models.IntegerField(primary_key=True, verbose_name='id de Categoria')
    NombredCategoria = models.CharField(max_length=15, verbose_name='Tipo usuario')

    def str(self):
        return self.NombredCategoria


        

class Automovil(models.Model):

    patente =  models.CharField(primary_key=True,max_length=18, unique=True)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    imagen = models.ImageField(upload_to="automoviles",null=True)

    def str(self):
        return self.patente




