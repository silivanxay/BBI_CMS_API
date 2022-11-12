
from stock.models import Stock
from rest_framework import serializers
from django.utils.module_loading import import_string
from django.conf import settings


Option = import_string(settings.OPTIONS_MODELS)


class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ['id', 'name', 'type', 'value', 'required']
        # fields = ['id', 'name', 'type', 'value', 'required']


class StockSerializer(serializers.ModelSerializer):
    option = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = ['id', 'num_in_stock', 'low_stock_threshold', 'product', 'option']
