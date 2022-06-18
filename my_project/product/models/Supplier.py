from django.db import models


class Supplier(models.Model):
    objects = models.Manager()
    name_supplier = models.CharField(max_length=50, unique=True)
    brands = models.CharField(max_length=100)
    supplier_price = models.FileField(blank=True, null=True)

    def __str__(self):
        self.name_supplier
