from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializers
from .models import Todo

# Create your views here.

# getting the serializer we made in serializers.py, and specifying what queryset we'll be serializing
class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()

