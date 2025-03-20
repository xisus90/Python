from django.db import models

from app.products.domain.value_objects.product_name import ProductName
from app.products.domain.value_objects.product_price import ProductPrice

class Product(models):
    id = models.AutoField(primary_key=True)
    nombre = ProductName
    descripcion = models.TextField(blank=True, null=True)
    precio = ProductPrice
    activo = models.BooleanField(default=True)
    imagen = models.URLField(blank=True, null=True)
    stock = models.IntegerField(default=0)