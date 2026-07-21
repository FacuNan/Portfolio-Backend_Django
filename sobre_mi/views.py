from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import SobreMi
from .serializers import SobreMiSerializer

class SobreMiViewSet(viewsets.ModelViewSet):
    queryset = SobreMi.objects.all()
    serializer_class = SobreMiSerializer