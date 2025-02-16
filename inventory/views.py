from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import F, ExpressionWrapper, BooleanField
from .models import Product, Sale, SaleItem, Purchase, PurchaseItem
from .forms import ProductForm, SaleForm, PurchaseForm, InventoryForm

# Home page
def home(request):
    return render(request, 'inventory/home.html')

# ------------------------------
# Product Management Views
# ------------------------------

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save new product
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit_product.html', {'form': form})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory/delete_product.html', {'product': product})

def inventory_list(request):
    products = Product.objects.all()
    low_stock = products.annotate(
        is_low_stock=ExpressionWrapper(F('quantity') < 5, output_field=BooleanField())
    )
    return render(request, 'inventory/inventory_list.html', {'products': products, 'low_stock': low_stock})

def update_inventory(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm(instance=product)
    return render(request, 'inventory/update_inventory.html', {'form': form})

# ------------------------------
# Sales Views (Decrease Inventory)
# ------------------------------

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'inventory/sale_list.html', {'sales': sales})

def view_sale(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    sale_items = sale.saleitem_set.select_related('product')
    for item in sale_items:
        item.subtotal = item.product.price * item.quantity
    return render(request, 'inventory/view_sale.html', {'sale': sale, 'sale_items': sale_items})

def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            # Save the Sale instance to generate a primary key
            sale = form.save()

            # Retrieve the cart from the session
            cart = request.session.get('cart', {})
            if not cart:
                return redirect('sale_list')

            # Create SaleItem instances for each item in the cart
            for id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=id)
                except Product.DoesNotExist:
                # Handle the case where the product doesn't exist
                    continue
                product = Product.objects.get(id=id)
                SaleItem.objects.create(sale=sale, product=product, quantity=quantity)
                product.adjust_inventory(-quantity)  # Decrease inventory

            # Clear the cart from the session
            request.session['cart'] = {}

            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'inventory/add_sale.html', {'form': form})


def process_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            # Save the Sale instance
            sale = form.save()

            # Retrieve product and quantity from the form
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']

            # Create and save the SaleItem instance
            SaleItem.objects.create(sale=sale, product=product, quantity=quantity)

            # Adjust the product's inventory
            product.quantity -= quantity
            product.save()

            return redirect('sale_success')
    else:
        form = SaleForm()
    return render(request, 'sales/sale_form.html', {'form': form})
# ------------------------------
# Purchase Views (Increase Inventory)
# ------------------------------

def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'inventory/purchase_list.html', {'purchases': purchases})

def view_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    purchase_items = purchase.purchaseitem_set.all()
    for item in purchase_items:
        item.subtotal = item.product.price * item.quantity
    return render(request, 'inventory/view_purchase.html', {'purchase': purchase, 'purchase_items': purchase_items})

def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            cart = request.session.get('cart', {})
            for id, quantity in cart.items():
                product = Product.objects.get(id=id)
                PurchaseItem.objects.create(purchase=purchase, product=product, quantity=quantity)
                product.adjust_inventory(quantity)  # Increase inventory
            request.session['cart'] = {}
            return redirect('purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'inventory/add_purchase.html', {'form': form})
