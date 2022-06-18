import uuid
from django.db import models


class Product(models.Model):
    objects = models.Manager()
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image_product = models.ImageField(blank=True, null=True)
    product_name = models.CharField(max_length=100, unique=True)
    product_description = models.TextField(null=True, max_length=300)
    count = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=1.0)
    url = models.URLField(max_length=200)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.product_name
