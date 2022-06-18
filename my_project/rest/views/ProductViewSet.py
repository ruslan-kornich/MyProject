from product.models.Product import Product
from rest.serializers import ProductModelSerializer
from rest_framework import viewsets
from rest.views.ProductPagination import ProductPagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
