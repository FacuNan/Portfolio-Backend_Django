from rest_framework import serializers
from .models import Educacion

class EducacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educacion
        fields = '__all__'

    