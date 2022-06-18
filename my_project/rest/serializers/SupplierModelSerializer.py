from product.models.Supplier import Supplier
from rest_framework import serializers

class SupplierModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name_supplier', 'brands']