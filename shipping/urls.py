from django.urls import path
from . import views

app_name = 'shipping'  # Додаємо namespace для уникнення конфліктів з іншими апками

urlpatterns = [
    path('address/', views.add_shipping, name='add_shipping'),
    path('edit/', views.edit_shipping, name='edit_shipping'),
    path('method/', views.choice_shipping, name='choice_shipping'),
    path('set-default/', views.set_default_address, name='set_default_address'),  # Додавання нового маршруту
]
