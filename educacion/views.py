from django.shortcuts import render
from rest_framework import viewsets
from .models import Educacion
from .serializers import EducacionSerializer

class EducacionViewSet(viewsets.ModelViewSet):
    queryset = Educacion.objects.all()
    serializer_class = EducacionSerializer

