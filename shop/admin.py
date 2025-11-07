# shop/admin.py
from django.contrib import admin
from .models import Product, Newsletter, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "price")
    search_fields = ("name", "brand")

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    search_fields = ("email",)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "quantity", "price")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "total_price", "payment_method", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("payment_method", "created_at")
    inlines = [OrderItemInline]
