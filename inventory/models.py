
# Create your models here.
from django.db import models

class Product(models.Model):
    """Setting up the product class. 

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    product_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (ID: {self.product_id})"
    

class Inventory(models.Model):
    """Setting up the inventory Class

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def get_low_stock(self, threshold=5):
        """This will show low stock items. Defaults to 5, but can be set to another amount
        if the optional threshold argument is added.

        Args:
            threshold (int, optional): _description_. Defaults to 5.

        Returns:
            _type_: _description_
        """
        return Product.objects.filter(quantity__lt=threshold)

    def __str__(self):
        return f"Inventory for {self.product.name}"
    
class Order(models.Model):
    """This Order class handles the settings for selecting the products and order_id
    and the total_cost of a given order.

    Args:
        models (_type_): _description_
    """
    order_id = models.CharField(max_length=50, unique=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_total(self):
        """This will calculate the total for your orders.
        """
        self.total_cost = sum(item.product.price * item.quantity for item in self.orderitem_set.all())
        self.save()

class OrderItem(models.Model):
    """This type contains order, product, and quantity.

    Args:
        models (_type_): _description_
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

