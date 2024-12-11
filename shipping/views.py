from django.shortcuts import render, redirect
from . import models

def add_shipping(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        street = request.POST.get('street')
        house_number = request.POST.get('house_number')
        
        new_address = models.Address(
            city=city,
            zip_code=zip_code,
            street=street,
            house_number=house_number
        )
        new_address.save()
        return redirect('shipping:choice_shipping')  
    return render(request, 'shipping/address_form.html')  

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
    
    return render(request, 'shipping/address_form.html', {'address': address})  

def choice_shipping(request):
    if request.method == 'POST':
        selected_method = request.POST.get('shipping-method')
        return redirect('success_page')  
    shipping_methods = models.ShippingMethod.objects.all()
    return render(request, 'shipping/choice_shipping.html', {'shipping_methods': shipping_methods})  