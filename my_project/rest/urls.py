from django.urls import include, path
from rest_framework import routers
from rest.views.ProductViewSet import ProductViewSet
from rest.views.SupplierViewSet import SupplierViewSet
from rest.views.ContactView import ContactView

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)
router.register(r'supplier', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contact/', ContactView.as_view(), name='contact'),
]