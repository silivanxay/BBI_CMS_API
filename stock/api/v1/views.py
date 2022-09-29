from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from stock.models import Option, Stock
from .serializers import StockSerializer, OptionSerializer

class StockListCreateAPIView(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class OptionListCreateAPIView(ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
