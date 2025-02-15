from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """This form is for products.

    Args:
        forms (_type_): _description_
    """
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'quantity']
