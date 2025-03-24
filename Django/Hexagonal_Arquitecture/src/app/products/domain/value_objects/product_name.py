from django.db import models
from django.core.exceptions import ValidationError

class ProductsName(models.Model):

    value = models.CharField(max_length=50, verbose_name="Valor del producto")

    def clean(self):
        if not self.value or not self.value.strip():
            raise ValidationError("No puedes dejar el campo vacio")
        if len(self.value) >= 50:
            raise ValidationError("El Nombre no puede exceder los 50 caracteres")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __eq__(self, other):
        return isinstance(other, ProductsName) and self.value == other.value
    
    def __str__(self):
        return self.value

    class Meta:
        abstract = True