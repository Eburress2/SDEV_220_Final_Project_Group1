from django.db.models import F
from django import forms
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product, Inventory
from django.core.exceptions import ValidationError

from inventory import models

class HomePageView(TemplateView):
    template_name = 'inventory/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_product_list'] = Product.objects.order_by('-id')[:5]
        context['low_stock_product_list'] = Inventory.objects.filter(quantity__lt=F('low_stock_threshold'))
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'inventory/category_list.html'
    context_object_name = 'categories'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name=name).exists():
            raise ValidationError('A category with this name already exists.')
        return name

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_create.html'
    success_url = reverse_lazy('inventory:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_form.html'
    success_url = reverse_lazy('inventory:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'inventory/category_confirm_delete.html'
    success_url = reverse_lazy('inventory:category_list')
    

class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Product.objects.filter(name=name).exists():
            raise ValidationError('A product with this name already exists.')
        return name


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
    

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductInventoryForm
    template_name = 'inventory/product_create.html'
    success_url = reverse_lazy('inventory:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductInventoryForm
    template_name = 'inventory/product_update.html'
    success_url = reverse_lazy('inventory:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('inventory:product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventory/product_detail.html'
    context_object_name = 'product'


class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventory_items'

class InventoryCreateView(CreateView):
    model = Inventory
    template_name = 'inventory/inventory_create.html'
    fields = ['product', 'quantity', 'low_stock_threshold']
    success_url = reverse_lazy('inventory:inventory_list')

class InventoryUpdateView(UpdateView):
    model = Inventory
    template_name = 'inventory/inventory_update.html'
    fields = ['product', 'quantity', 'low_stock_threshold']
    success_url = reverse_lazy('inventory:inventory_list')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:inventory_list')


