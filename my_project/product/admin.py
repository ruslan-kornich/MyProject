from django.contrib import admin
from product.models import Supplier, Client, Product

# Register your models here.


#admin.site.register(Client)
admin.site.register(Supplier)
admin.site.register(Product)
