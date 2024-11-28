from django.contrib import admin
from .models import Product, Category

@admin.register(Product)  # Використовуємо декоратор для реєстрації Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'category')  # Додали 'category' до списку
    search_fields = ('title',)
    list_filter = ('category',)  # Додати фільтр по категорії в адмінці

admin.site.register(Category)  # Окрема реєстрація для Category
