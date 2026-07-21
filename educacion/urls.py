from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducacionViewSet


router = DefaultRouter()
router.register(r'educacion', EducacionViewSet, basename='educacion')
urlpatterns = [
    path('', include(router.urls)),
]   