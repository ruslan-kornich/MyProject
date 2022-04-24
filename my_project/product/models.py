from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Product(models.Model):
    shop = models.Manager()
    image_product = models.ImageField(blank=True, null=True)
    product_name = models.CharField(max_length=100, unique=True)
    product_description = models.TextField(null=True, max_length=300)
    count = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=1.0)
    url = models.URLField(max_length=200)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True)


class Supplier(models.Model):
    name_supplier = models.CharField(max_length=50, unique=True)
    brands = models.CharField(max_length=100)
    supplier_price = models.FileField(blank=True, null=True)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    second_email = models.EmailField(null=True)
    name = models.CharField(max_length=64, null=True)
    invoice = models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')
    user_uuid = models.UUIDField(editable=False, null=True)
    discount_size = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    client_ip = models.GenericIPAddressField(blank=True, null=True, protocol="IPv4")

    def __str__(self):
        return self.name
