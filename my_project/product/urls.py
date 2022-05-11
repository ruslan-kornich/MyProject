from django.urls import path
from product import views

urlpatterns = [
    path('upload/', views.upload_data, name='upload'),
    path('filter/', views.FilterView.as_view(), name='filter'),
    path('exclude/', views.ExcludeView.as_view(), name='exclude'),
    path('orderby/', views.OrderByView.as_view(), name='orderby'),
    path('all/', views.AllView.as_view(), name='all'),
    ]
