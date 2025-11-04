from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    contacto = models.CharField(max_length=15)


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9000, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.CASCADE)   