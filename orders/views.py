from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem

@login_required
def create_order(request):
    if request.method == 'POST':
        items = request.POST.getlist('items')  
        quantities = request.POST.getlist('quantities')  
        prices = request.POST.getlist('prices')  

        if not items or not quantities or not prices:
            return render(request, 'order_form.html', {'error': 'Заповніть усі поля'})

        order = Order.objects.create(user=request.user)
        for product, quantity, price in zip(items, quantities, prices):
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=int(quantity),
                price_per_item=float(price)
            )
        return redirect('order_history')  
    return render(request, 'order_form.html')  

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_created')  
    return render(request, 'order_history.html', {'orders': orders})
