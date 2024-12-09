from django.db import models
from django.contrib.auth.models import User  

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','pending',),
        ('completed','comleted',),
        ('canceled','canceled',),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='User')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Status')
    def __str__(self):
        return f"Order #{self.id} ({self.get_status_display()})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Orders')
    product = models.CharField(max_length=255, verbose_name='Product') 
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price for unit')

    def get_total_price(self):
        return self.quantity * self.price_per_item
    def __str__(self):
        return f"{self.quantity} x {self.product}"
