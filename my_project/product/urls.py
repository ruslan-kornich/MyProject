from django.urls import path
from product import views

urlpatterns = [
    path('create-product/', views.create_product, name='create_product'),
    path('create-client/', views.create_client, name='create_client'),
    path('get_camera/', views.get_camera, name='get_camera'),
    ]