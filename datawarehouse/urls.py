from rest_framework import routers
from django.urls import path, include
from .viewsets import ClientesViewSet, ServicosViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet)
router.register(r'servicos', ServicosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
