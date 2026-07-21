from django.shortcuts import render
from rest_framework import viewsets
from .models import Experiencia
from .serializers import ExperienciaSerializer


class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer

