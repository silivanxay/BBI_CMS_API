
from django.db import models
from product.models import Product
from enum import Enum



class Optiontype(Enum):
    Boolean = "True / False"
    Text = "Text"
    Integer = "Integer"
    Float = "Float"
    Date = "Date"

class Option(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(choices=[(tag.name, tag.value) for tag in Optiontype], max_length=10, default='Text', blank=True)
    value = models.CharField(max_length=255, blank=True)
    required = models.BooleanField(blank=True)


    class Meta:

        verbose_name = ("option")
        verbose_name_plural = ("options")

    def __str__(self):
       return self.name

class Stock(models.Model):
    option = models.ManyToManyField("Option", blank=True)
    num_in_stock = models.IntegerField()
    low_stock_threshold = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='stock')
   

    class Meta:
     
        verbose_name = ("stock")
        verbose_name_plural = ("stocks")


    def __str__(self):
        return str (self.option)














