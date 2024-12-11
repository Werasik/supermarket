from django.urls import path
from . import views

urlpatterns = [
    path('address/', views.add_shipping, name='add_shipping'),  
    path('edit/', views.edit_shipping, name='edit_shipping'),  
    path('method/', views.choice_shipping, name='choice_shipping'),  
]
