from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExperienciaViewSet

router = DefaultRouter()
router.register(r'experiencia', ExperienciaViewSet, basename='experiencia')

urlpatterns = [
    path('', include(router.urls)),
]