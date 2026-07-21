from django.shortcuts import render
from rest_framework import viewsets
from .models import Proyecto
from .serializers import ProyectoSerializer
from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD','OPTIONS']:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff

# Create your views here.
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

