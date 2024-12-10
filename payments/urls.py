from django.urls import path
from . import views
path = [
      path('create/', views.create_payment, name='create_payment'),
      path('payment_success/', views.payment_success, name='payment_success'),
      path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
]