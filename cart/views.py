from django.shortcuts import render, redirect, get_object_or_404
from Products.models import Product  
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)  
    cart, created = Cart.objects.get_or_create(user=request.user)  
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:  
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, product=product)
        cart_item.delete()
    except (Product.DoesNotExist, Cart.DoesNotExist, CartItem.DoesNotExist):
        pass  
    return redirect('cart')
