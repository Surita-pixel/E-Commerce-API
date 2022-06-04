# Django 
from django.shortcuts import render
from django.http import HttpResponse

# Django Rest Framework
from rest_framework import viewsets

# Moduls
from main_app.models import Item
from main_app.serializers import ItemSerializer


def index(request):
   """this funtion will see if the endpoint is
      main_app/
      and just print a hello word
   """
   return HttpResponse("Hello word")

class ItemApiView(viewsets.ModelViewSet):
   queryset= Item.objects.all()
   serializer_class= ItemSerializer