from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import SobreMi
from .serializers import SobreMiSerializer
from rest_framework.permissions import BasePermission

class IsAuthenticatedReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff
    
class SobreMiViewSet(viewsets.ModelViewSet):
    queryset = SobreMi.objects.all()
    serializer_class = SobreMiSerializer

    # Add IsAdminUser permission for admin actions
    permission_classes = [IsAuthenticatedReadOnly]