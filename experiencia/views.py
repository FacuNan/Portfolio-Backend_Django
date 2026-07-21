from django.shortcuts import render
from rest_framework import viewsets
from .models import Experiencia
from .serializers import ExperienciaSerializer
from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):
    
        def has_permission(self, request, view):
            if request.method in ['GET', 'HEAD','OPTIONS']:
                return True
            return request.user and request.user.is_authenticated and request.user.is_staff

class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

