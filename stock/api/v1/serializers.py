
from stock.models import Option, Stock
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Stock
        fields = "__all__"

class OptionSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Option
        fields = "__all__"





