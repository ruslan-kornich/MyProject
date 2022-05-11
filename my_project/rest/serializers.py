from product.models import Product, Supplier
from rest_framework import serializers


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SupplierModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name_supplier', 'brands']