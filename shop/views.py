from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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

# 🔐 User Login 
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('shop:login')

    return render(request, 'shop/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('shop:home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'shop/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('shop:login')