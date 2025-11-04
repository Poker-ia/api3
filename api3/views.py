from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductoSerializer, ProveedorSerializer
from .models import Producto, Proveedor

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
