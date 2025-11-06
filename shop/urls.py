# shop/urls.py

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us, name='contact'),
    path("subscribe/", views.newsletter_subscribe, name="subscribe"),

]
