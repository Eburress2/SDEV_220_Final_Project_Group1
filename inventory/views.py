"""
Views for the inventory app.

This file contains the view classes for the inventory app, 
handling the logic for displaying templates,
processing forms, and interacting with the models. 
Each view class corresponds to a specific URL pattern
and provides the necessary context and functionality 
for the associated template.
"""


from django.db.models import F
from django import forms
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product, Inventory
from django.core.exceptions import ValidationError

from inventory import models


# Home page view
class HomePageView(TemplateView):
    template_name = 'inventory/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_product_list'] = Product.objects.order_by('-id')[:5]
        context['low_stock_product_list'] = Inventory.objects.filter(quantity__lt=F('low_stock_threshold'))
        return context


# List view for categories
class CategoryListView(ListView):
    model = Category
    template_name = 'inventory/category_list.html'
    context_object_name = 'categories'


# Form for creating and updating categories
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name=name).exists():
            raise ValidationError('A category with this name already exists.')
        return name


# Create view for categories
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_create.html'
    success_url = reverse_lazy('inventory:category_list')


# Update view for categories
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_form.html'
    success_url = reverse_lazy('inventory:category_list')


# Delete view for categories
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'inventory/category_confirm_delete.html'
    success_url = reverse_lazy('inventory:category_list')
    

# List view for products
class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'


# Form for creating and updating products
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Product.objects.filter(name=name).exists():
            raise ValidationError('A product with this name already exists.')
        return name


# Form for creating products with inventory
class ProductInventoryForm(forms.ModelForm):
    quantity = forms.IntegerField(initial=0, required=False)

    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'quantity']

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
            Inventory.objects.create(product=product, quantity=self.cleaned_data['quantity'])
        return product
    

# Create view for products
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductInventoryForm
    template_name = 'inventory/product_create.html'
    success_url = reverse_lazy('inventory:product_list')


# Update view for products
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductInventoryForm
    template_name = 'inventory/product_update.html'
    success_url = reverse_lazy('inventory:product_list')


# Delete view for products
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('inventory:product_list')


# Detail view for products
class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventory/product_detail.html'
    context_object_name = 'product'


# List view for inventory items
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory_items'


# Create view for inventory items
class InventoryCreateView(CreateView):
    model = Inventory
    template_name = 'inventory/inventory_create.html'
    fields = ['product', 'quantity', 'low_stock_threshold']
    success_url = reverse_lazy('inventory:inventory_list')


# Update view for inventory items
class InventoryUpdateView(UpdateView):
    model = Inventory
    template_name = 'inventory/inventory_update.html'
    fields = ['product', 'quantity', 'low_stock_threshold']
    success_url = reverse_lazy('inventory:inventory_list')


# Delete view for inventory items
class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:inventory_list')


