from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Products.models import Product
from .models import Cart, CartItem


@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_price = sum(item.total_price for item in cart_items)

    # Логування для діагностики
    print("Cart Items:", cart_items)
    print("Total Price:", total_price)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })
@login_required
def add_to_cart(request, product_id):
    # Отримуємо продукт або повертаємо 404, якщо не знайдено
    product = get_object_or_404(Product, id=product_id)
    # Отримуємо або створюємо кошик для користувача
    cart, _ = Cart.objects.get_or_create(user=request.user)
    # Отримуємо або створюємо елемент кошика
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1  # Якщо товар вже є, збільшуємо кількість
    cart_item.save()  # Зберігаємо зміни
    return redirect('cart_detail')  # Переходимо до кошика

@login_required
def remove_from_cart(request, product_id):
    # Отримуємо кошик користувача
    cart = Cart.objects.get(user=request.user)
    # Отримуємо елемент кошика
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

    # Зменшуємо кількість товару
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()  # Зберігаємо зміни
    else:
        # Якщо кількість дорівнює 1, видаляємо елемент
        cart_item.delete()
    
    return redirect('cart_detail')  # Переходимо назад у кошик
