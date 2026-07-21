from rest_framework import serializers  
from .models import SobreMi

class SobreMiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SobreMi
        fields = '__all__'
        