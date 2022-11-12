
from django.db import models
from product.models import Product

class Stock(models.Model):
    num_in_stock = models.IntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='stock')
   

    class Meta:

        verbose_name = ("stock")
        verbose_name_plural = ("stocks")

    # def __str__(self):
    #     return str (self.num_in_stock)














