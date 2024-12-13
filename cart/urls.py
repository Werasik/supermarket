from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_detail'),  # Головна сторінка кошика
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Додавання до кошика
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Видалення з кошика
]
