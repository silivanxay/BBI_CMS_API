
from django.db import models
from stock.models import Stock
from enumchoicefield import ChoiceEnum, EnumChoiceField


class Optiontype(ChoiceEnum):
    Boolean = "True / False"
    Text = "Text"
    Integer = "Integer"
    Float = "Float"
    Date = "Date"

class Option(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = EnumChoiceField(Optiontype, default=Optiontype.Text)
    value = models.CharField(max_length=255, blank=True)
    required = models.BooleanField(blank=True)
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='option')

    class Meta:

        verbose_name = ("option")
        verbose_name_plural = ("options")

    def __str__(self):
       return self.name