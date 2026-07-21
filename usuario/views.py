from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import BasePermission
# Create your views here.

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff
    
    

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
