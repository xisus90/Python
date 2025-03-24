from django.db import models
from django.core.exceptions import ValidationError

class ProductsValue(models.Model):

    value = models.FloatField(verbose_name="Valor del producto")

    def clean(self):
        if self.value <=0:
            raise ValidationError("El precio no puede ser 0 o inferior")


    def __eq__(self, other):
        return isinstance(other, ProductsValue) and self.value == other.value
    
    def __str__(self):
        return f"{self.value:.2f}"

    class Meta:
        abstract = True