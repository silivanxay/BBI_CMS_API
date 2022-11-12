
from option.models import Option
from rest_framework import serializers
# from django.utils.module_loading import import_string
# from django.conf import settings


# Stock = import_string(settings.STOCK_MODELS)



# class StocksSerializer(serializers.ModelSerializer):
   
#     class Meta:
#         model = Stock
#         fields = ['id','num_in_stock', 'low_stock_threshold']

class OptionSerializer(serializers.ModelSerializer):
    # stock = StocksSerializer(many=True, read_only=True)
  
    class Meta:
        model = Option
        fields = '__all__'
        # fields = ['id', 'name', 'type', 'value', 'required',]





