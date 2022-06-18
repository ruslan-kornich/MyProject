from django.contrib import admin
from product.models.Supplier import Supplier
from product.models.Product import Product
from product.models.Client import Client

# Register your models here.


admin.site.register(Client)
admin.site.register(Supplier)
admin.site.register(Product)
