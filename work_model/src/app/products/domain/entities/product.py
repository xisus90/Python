from django.db import models

from app.products.domain.value_objects.product_name import ProductsName
from app.products.domain.value_objects.product_price import ProductsValue
from app.products.domain.value_objects.stock import ProducstStock

class Product(models):
    id = models.AutoField(primary_key=True)
    nombre = ProductsName
    descripcion = models.TextField(blank=True, null=True)
    precio = ProductsValue
    activo = models.BooleanField(default=True)
    imagen = models.URLField(blank=True, null=True)
    stock = ProducstStock