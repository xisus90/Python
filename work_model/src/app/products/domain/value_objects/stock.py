from django.db import models
from django.core.exceptions import ValidationError

class ProducstStock(models.Model):

    value = models.IntegerField(verbose_name="Cantidad en stock")

    def clean(self):
        if self.value < 0:
            raise ValidationError("La cantidad de stock no puede ser inferior a 0")

    def __eq__(self, other):
        return isinstance(other, ProducstStock) and self.value == other.value
    
    def __str__(self):
        return str(self.value)
    
    class Meta:
        abstract = True