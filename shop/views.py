from decimal import Decimal
import json

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Product, Newsletter, Order, OrderItem  # ✅ include order models


# 🏠 Home Page — Displays only 4 featured products
def home(request):
    products = Product.objects.all()[:4]
    return render(request, 'shop/home.html', {'products': products})


# 🔍 Product Details Page
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_details.html', {'product': product})


# 🧭 All Products page (match navbar: shop:products)
def products(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})


# 🛒 Cart Page
def cart(request):
    return render(request, 'shop/cart.html')


# 💳 Checkout Page (only for logged-in users)
@login_required(login_url='accounts:login')
def checkout(request):
    return render(request, 'shop/checkout.html')


# 🧾 Place Order — persists order & items
@login_required(login_url='accounts:login')
def place_order(request):
    if request.method != "POST":
        messages.error(request, "Invalid request.")
        return redirect('shop:checkout')

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    phone = request.POST.get("phone", "").strip()
    address = request.POST.get("address", "").strip()
    payment_method = request.POST.get("payment_method", "COD").upper()
    raw = request.POST.get("order_data", "[]")
    try:
        items_in = json.loads(raw)
        if not isinstance(items_in, list) or len(items_in) == 0:
            raise ValueError
    except Exception:
        messages.error(request, "Your cart is empty or invalid.")
        return redirect('shop:checkout')
    line_items = []
    total = Decimal("0.00")

    for it in items_in:
        try:
            pid = int(it.get("id"))
            qty = int(it.get("quantity", 1))
            if qty <= 0:
                continue
        except (TypeError, ValueError):
            continue

        product = get_object_or_404(Product, id=pid)
        price = product.price
        line_items.append((product, qty, price))
        total += (price * qty)

    if not line_items:
        messages.error(request, "No valid items to place an order.")
        return redirect('shop:checkout')
    if not all([name, email, phone, address]):
        messages.error(request, "Please fill all shipping details.")
        return redirect('shop:checkout')
    order = Order.objects.create(
        user=request.user,
        name=name,
        email=email,
        phone=phone,
        address=address,
        payment_method=payment_method,
        total_price=total
    )

    bulk = [
        OrderItem(order=order, product=prod, quantity=qty, price=price)
        for (prod, qty, price) in line_items
    ]
    OrderItem.objects.bulk_create(bulk)

    messages.success(request, f"Order #{order.id} placed successfully 🎉")
    return redirect('shop:order_success', order_id=order.id)


@login_required(login_url='accounts:login')
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_success.html', {'order': order})


def about_us(request):
    return render(request, 'shop/about.html')


def contact_us(request):
    return render(request, 'shop/contact.html')

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


def newsletter_subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, "You are already subscribed!")
        else:
            Newsletter.objects.create(email=email)
            messages.success(request, "Subscribed successfully!")

        return redirect(request.META.get("HTTP_REFERER", "/"))

    return redirect("/")
