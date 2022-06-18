from django.contrib import admin
from product.models.Contact import Contact


# Register your models here.
@admin.register(Contact)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
