from django import forms
from django.core.exceptions import ValidationError
from .models import Product, Sale, Purchase

# class ProductForm(forms.ModelForm):
#     """Form for creating and editing products."""
#     class Meta:
#         model = Product
#         # Assuming your Product model now has these fields:
#         fields = ['id', 'name', 'price', 'quantity']

# class SaleForm(forms.ModelForm):
#     product = forms.ModelChoiceField(queryset=Product.objects.all(), label="Select Product")
#     quantity = forms.IntegerField(min_value=1, label="Quantity")

#     class Meta:
#         model = Sale
#         fields = []

#     def clean(self):
#         cleaned_data = super().clean()
#         product = cleaned_data.get('product')
#         quantity = cleaned_data.get('quantity')

#         if product and quantity:
#             if quantity > product.quantity:
#                 raise ValidationError(f"Requested quantity for {product.name} exceeds available stock.")
#         return cleaned_data

# class PurchaseForm(forms.ModelForm):
#     """
#     Form for recording a purchase transaction.
#     The product and quantity are used to create a PurchaseItem in the view.
#     """
#     product = forms.ModelChoiceField(
#         queryset=Product.objects.all(), 
#         label="Select Product"
#     )
#     quantity = forms.IntegerField(min_value=1, label="Quantity")

#     class Meta:
#         model = Purchase
#         # Similarly, if your Purchase model auto-generates purchase_date and total_price, leave fields empty.
#         fields = []

# class InventoryForm(forms.ModelForm):
#     """Form for updating the inventory quantity of a product."""
#     class Meta:
#         model = Product
#         fields = ['quantity']
