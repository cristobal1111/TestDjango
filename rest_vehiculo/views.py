from re import S
from django.shortcuts import render
from django.utils.encoding import DjangoUnicodeDecodeError
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Vehiculo
from .serializers import VehiculoSerializers

#vistas

@csrf_exempt
@api_view(['GET','POST'])
def lista_vehiculos(request):
    """
    Lista todos los vehículos
    """
    if (request.method=='GET'):
        vehiculo = Vehiculo.objects.all()
        serializers = VehiculoSerializers(vehiculo, many=True)
        return Response(serializers.data)
    elif (request.method=='POST'):
        data = JSONParser().parse(request)
        serializers = VehiculoSerializers(data=data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_vehiculo(request,id):
    """
    GET, update o delete de un vehiculo en particular
    """
    try: #verificar que patente ingresada existe
        vehiculo = Vehiculo.objects.get(patente=id)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        serializer = VehiculoSerializers(vehiculo)
        return Response(serializer.data)
    if (request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = VehiculoSerializers(vehiculo, data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        Vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)