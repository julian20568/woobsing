#from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from PalabrasClaves.models import Palabras
from PalabrasClaves.serializers import PalabrasSerializers
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def MetPalabras(request):
    if request.method == 'GET':
        Pal = Palabras.objects.all()
        serializer = PalabrasSerializers(Pal,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        serializer = PalabrasSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)