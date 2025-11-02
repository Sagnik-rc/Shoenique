from django.test import TestCase
from shop.models import Product

# Create your tests here.

Product.objects.create(
    name="Test Shoe",
    price=99.99,
    description="Test Description"
)
exit()
