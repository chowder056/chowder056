from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status

from django.views.decorators.csrf import csrf_exempt
from caosnews.models import *
from .serializers import *


@csrf_exempt
@api_view(['GET','POST'])
def lista_corta(request):
    """ LISTA"""
    if request.method=='GET':
        serializar = cortaSerializers(corta.objects.all(), many=True)  
        return Response(serializar.data)
    elif request.method=='POST':
        info= JSONParser().parse(request)
        serializar = cortaSerializers(data=info)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle(request, id):
    try:
        caos= corta.objects.get(id=id)
    except corta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializar = cortaSerializers(caos)
        return Response(serializar.data)

    elif request.method=='PUT':
        nuevo = JSONParser().parse(request)
        serializar = cortaSerializers(caos, data=nuevo)
        if serializers.is_valid():
            serializar.save()
            return Response(serializar.data)
        else:
            return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        caos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Buscar todo  
@api_view(['GET',])
def ver_todo(request):
    try:
         caos = caosnews.objects.all()
    except caosnews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializar = caosSerializers(caos, many=True)
        return Response(serializar.data)

#Buscar por rut 
@api_view(['GET',])
def buscar_colab(request,rut):
    try:
         caos = caosnews.objects.filter(rut=rut)
    except caosnews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializar = caosSerializers(caos, many=True)
        return Response(serializar.data)

#Buscar por nombre
@api_view(['GET',])      
def buscar_colab_nombre(request,nombre):
    try:
        caos = caosnews.objects.filter(nombre_caosnews__contains=nombre)
    except caosnews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializar = caosSerializers(caos, many = True)
        return Response (serializar.data)