from rest_framework import serializers
from .models import Producto, Proveedor

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Producto
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'