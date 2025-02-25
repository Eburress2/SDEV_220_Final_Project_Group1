from django.db import models
from django.forms import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)  # Changed to OneToOneField
    quantity = models.IntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=10)

    @property
    def is_low_stock(self):
        return self.quantity < self.low_stock_threshold

    def clean(self):
        if self.quantity < 0:
            raise ValidationError("Quantity cannot be negative")

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"  # Fixed to use product's name
    