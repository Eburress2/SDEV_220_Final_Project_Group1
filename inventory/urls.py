from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    HomePageView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    InventoryListView,
    InventoryCreateView,
    InventoryUpdateView,
    InventoryDeleteView

)
app_name = "inventory"
urlpatterns = [
    # Home page
    path('', HomePageView.as_view(), name='home'),  # Add this line

    # Categories
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

        # Products
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Inventory
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory/new/', InventoryCreateView.as_view(), name='inventory_create'),
    path('inventory/<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),
]