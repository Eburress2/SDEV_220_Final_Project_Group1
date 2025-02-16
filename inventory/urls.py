from django.urls import path
from .views import (
    home,
    process_sale,
    product_list,
    add_product,
    edit_product,
    delete_product,
    inventory_list,
    update_inventory,
    sale_list,
    add_sale,
    view_sale,
    purchase_list,
    add_purchase,
    view_purchase,
)

urlpatterns = [
    path('', home, name='home'),
    
    # Product endpoints
    path('products/', product_list, name='product_list'),
    path('products/add/', add_product, name='add_product'),
    path('products/edit/<int:id>/', edit_product, name='edit_product'),
    path('products/delete/<int:id>/', delete_product, name='delete_product'),
    
    # Inventory endpoint
    path('inventory/', inventory_list, name='inventory_list'),
    path('inventory/update/<str:id>/', update_inventory, name='update_inventory'),
    
    # Sales endpoints (decrease inventory)
    path('sales/', sale_list, name='sale_list'),
    path('sales/add/', add_sale, name='add_sale'),
    path('sales/view/<int:sale_id>/', view_sale, name='view_sale'),
    path('sales/process/', process_sale, name='process_sale'),
    
    # Purchases endpoints (increase inventory)
    path('purchases/', purchase_list, name='purchase_list'),
    path('purchases/add/', add_purchase, name='add_purchase'),
    path('purchases/view/<int:purchase_id>/', view_purchase, name='view_purchase'),
]
