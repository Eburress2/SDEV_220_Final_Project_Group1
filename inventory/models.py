
from django.db import models
from django import forms
from django.forms import inlineformset_factory

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def adjust_inventory(self, quantity_change):
        """Adjust the product's inventory by the specified quantity change."""
        self.quantity += quantity_change
        self.save()

    def __str__(self):
        return f"{self.name}"
    
class Purchase(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class PurchaseItem(models.Model):
    """When purchasing items, the quantity will increase."""
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Increase the product's inventory
        self.product.quantity += self.quantity
        self.product.save()
        super().save(*args, **kwargs)


class Sale(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

    def calculate_total_price(self):
        # Implement the logic to calculate total_price
        # For example, summing related SaleItem prices
        return sum(item.price for item in self.saleitem_set.all())

    
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['id', 'total_price']

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Decrease the product's inventory
        self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)


SaleItemFormSet = inlineformset_factory(
    Sale,
    SaleItem,
    fields=['product', 'quantity'],
    extra=1,  # Number of empty forms to display
    can_delete=True  # Allow deletion of sale items
)