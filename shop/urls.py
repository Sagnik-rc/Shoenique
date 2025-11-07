# shop/urls.py

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),  # if you have this
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('place-order/', views.place_order, name='place_order'),          # ✅ NEW
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),  # ✅ NEW
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact'),
    path("subscribe/", views.newsletter_subscribe, name="subscribe"),


]
