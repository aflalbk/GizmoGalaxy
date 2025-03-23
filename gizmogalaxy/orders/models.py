from django.db import models
from customers.models import Customer
from product.models import Product

# Create your models here.
class Order(models.Model):
    live = 1
    delete = 0
    delete_choices = ((live,'live'),(delete,'delete'))

    # Order status
    cart_stage = 0
    order_confirmed = 1
    order_prosessing = 2
    order_delivered = 3
    order_rejected = 4

    order_status_choice = ((order_confirmed,"order_confirmed"),(order_prosessing,"order_prosessing"),(order_delivered,"order_delivered"),(order_rejected,"order_rejected"))
    order_status = models.IntegerField(choices=order_status_choice, default=cart_stage)
    total_price = models.FloatField(default=0)

    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="orders")

    delete_status = models.IntegerField(choices=delete_choices, default=live)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"order-{self.id}-{self.owner.username}"

class OrderedItem(models.Model):
    product = models.ForeignKey(Product,related_name="added_items", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="added_items")
