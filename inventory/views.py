from django.shortcuts import redirect, render
from .models import Product, Inventory, Order
from .forms import ProductForm

# Create your views here.
def home(request):
    """This will take you to the inventory/home page.

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, 'inventory/home.html')

def product_list(request):
    """This will take you to the product list page.

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def add_product(request):
    """This will take you to the form to add a product.

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def inventory_list(request):
    """This will allow you to see a list of all items and low stock items.

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    inventory = Inventory.objects.all()
    low_stock = Inventory.objects.first().get_low_stock() if Inventory.objects.exists() else []
    return render(request, 'inventory/inventory_list.html', {'inventory': inventory, 'low_stock': low_stock})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'inventory/order_list.html', {'orders': orders})

