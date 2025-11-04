from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductoViewSet, ProveedorViewSet

router = DefaultRouter()

router.register(r'productos',ProductoViewSet)
router.register(r'proveedor',ProveedorViewSet)

urlpatterns = [
    path('', include(router.urls))
]