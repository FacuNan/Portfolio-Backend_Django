from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SobreMiViewSet

router = DefaultRouter()
router.register('sobre_mi', SobreMiViewSet, basename='sobre_mi')

urlpatterns =  [
    path('', include(router.urls))
]