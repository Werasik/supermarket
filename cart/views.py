from django.shortcuts import render, redirect
from Products.models import Product  # Імпортуємо модель продукту
from .models import Cart, CartItem

# Головна сторінка кошика
def cart_view(request):
    # Отримуємо або створюємо кошик для користувача
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Отримуємо всі товари в кошику
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Обчислюємо суму кошика
    total_price = sum(item.total_price for item in cart_items)
    
    # Повертаємо рендер із шаблоном
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

    
# Додати товар до кошика
def add_to_cart(request, product_id):
    try:
        # Отримуємо продукт за його ID
        product = Product.objects.get(id=product_id)
        
        # Отримуємо або створюємо кошик для користувача
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Створюємо або отримуємо товар у кошику
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        # Якщо товар вже є в кошику, збільшуємо його кількість
        cart_item.quantity += 1
        cart_item.price = product.price  # Оновлюємо ціну (якщо вона змінилася)
        cart_item.save()
        
        # Після додавання перенаправляємо на сторінку кошика
        return redirect('cart')
    
    except Product.DoesNotExist:
        # Якщо продукт не знайдено, перенаправляємо на головну сторінку або іншою логікою
        return redirect('home')  # або повернути на іншу сторінку за потреби

def remove_from_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
    except (Product.DoesNotExist, CartItem.DoesNotExist):
        pass
    return redirect('cart')
