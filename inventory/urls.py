from django.urls import path
from .views import add_product, home, product_list, inventory_list, order_list

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/add', add_product, name='add_product'),
    path('inventory/', inventory_list, name='inventory_list'),
    path('orders/', order_list, name='order_list'),
]
