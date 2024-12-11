from django.db import models

class ShippingMethod(models.Model):
    STANDARD = 'standard'
    EXPRESS = 'express'
    
    SHIPPING_CHOICES = [
        (STANDARD, 'Standart Shipping'),
        (EXPRESS, 'Ekspress Shipping'),
    ]
    
    name = models.CharField(
        max_length=20,
        choices=SHIPPING_CHOICES,
        default=STANDARD,
        verbose_name="Method Shipping"
    )

    def __str__(self):
        return dict(self.SHIPPING_CHOICES).get(self.name)


class Address(models.Model):
    city = models.CharField(max_length=100, verbose_name="City")
    zip_code = models.CharField(max_length=10, verbose_name="Zip Code")
    street = models.CharField(max_length=255, verbose_name="Street")
    house_number = models.CharField(max_length=10, verbose_name="House number")

    def __str__(self):
        return f"{self.street} {self.house_number}, {self.city} {self.zip_code}"