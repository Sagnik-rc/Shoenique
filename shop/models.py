from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.name
