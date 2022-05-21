from django.urls import include, path
from rest_framework import routers
from rest import views

router = routers.SimpleRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'supplier', views.SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contact/', views.ContactView.as_view(), name='contact'),
]