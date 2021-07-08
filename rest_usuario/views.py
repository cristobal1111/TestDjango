from django.shortcuts import render
from django.utils.encoding import DjangoUnicodeDecodeError
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario
from .serializers import UsuarioSerializer

@csrf_exempt
@api_view(['GET','POST'])

def lista_usuarios(request):
    """
    Lista de usuarios registrados
    """
    if (request.method == 'GET'):
        usuario =  Usuario.objects.all()
        serializers =  UsuarioSerializer(usuario, many=True)
        return Response(serializers.data)
    elif (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializers = UsuarioSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)