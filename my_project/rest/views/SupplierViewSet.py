from product.models.Supplier import Supplier
from rest.serializers import SupplierModelSerializer
from rest_framework import viewsets


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer
