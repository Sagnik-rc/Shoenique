from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product

# 🏠 Home Page — Displays all products
def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

# 🔍 Product Details Page
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_details.html', {'product': product})

# 🛒 Cart Page
def cart(request):
    return render(request, 'shop/cart.html')

# 💳 Checkout Page (only for logged-in users)
@login_required(login_url='accounts:login')
def checkout(request):
    return render(request, 'shop/checkout.html')
