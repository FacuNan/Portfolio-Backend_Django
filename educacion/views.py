from django.shortcuts import render
from rest_framework import viewsets
from .models import Educacion
from .serializers import EducacionSerializer
from rest_framework.permissions import BasePermission 

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD','OPTIONS']:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff

class EducacionViewSet(viewsets.ModelViewSet):
    queryset = Educacion.objects.all()
    serializer_class = EducacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

