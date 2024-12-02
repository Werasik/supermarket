from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_all_products, name='index'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),  
    path('search_products/', views.search_by_name, name='search_products'),  
]
