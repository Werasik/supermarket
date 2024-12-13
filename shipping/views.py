from django.shortcuts import render, redirect
from . import models
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Address
from django.shortcuts import render, redirect, get_object_or_404
from .models import Address

from django.http import HttpResponseRedirect
from django.urls import reverse

def set_default_address(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        try:
            address = Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            return HttpResponseRedirect(reverse('shipping:add_shipping'))  # Перенаправлення на створення адреси

        # Позначаємо всі адреси як не за замовчуванням
        Address.objects.update(is_default=False)
        # Встановлюємо обрану адресу за замовчуванням
        address.is_default = True
        address.save()
        return redirect('index')  # Перенаправлення на головну сторінку

    addresses = Address.objects.all()  # Отримуємо всі адреси
    return render(request, 'select_default_address.html', {'addresses': addresses})


def add_shipping(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        street = request.POST.get('street')
        house_number = request.POST.get('house_number')
        country = request.POST.get('country')

        # Перевірка наявності всіх даних
        if not all([city, zip_code, street, house_number, country]):
            return render(request, 'add_shipping.html', {'error': 'Please fill in all fields.'})

        # Зберігаємо адресу
        new_address = Address(
            city=city,
            zip_code=zip_code,
            street=street,
            house_number=house_number,
            country=country
        )
        new_address.save()

        # Перенаправлення на вибір адреси за замовчуванням
        return redirect('shipping:set_default_address')

    return render(request, 'add_shipping.html')


def edit_shipping(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        address = models.Address.objects.get(id=address_id)
        address.city = request.POST.get('city')
        address.zip_code = request.POST.get('zip_code')
        address.street = request.POST.get('street')
        address.house_number = request.POST.get('house_number')
        address.save()
        return redirect('shipping:choice_shipping')
    
    address_id = request.GET.get('id')
    address = models.Address.objects.get(id=address_id)
    
    return render(request, 'address_form.html', {'address': address})  

def choice_shipping(request):
    if request.method == 'POST':
        selected_method = request.POST.get('shipping-method')
        return redirect('success_page')  
    shipping_methods = models.ShippingMethod.objects.all()
    return render(request, 'choice_shipping.html', {'shipping_methods': shipping_methods})  