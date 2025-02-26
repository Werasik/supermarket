from django.shortcuts import render, get_object_or_404
from .models import Product

def check_all_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product_detail.html', {'product': product})

def search_by_name(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.none()
    return render(request, 'search_by_name.html', {'products': products, 'query': query})
