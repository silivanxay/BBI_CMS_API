from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from stock.models import Stock
from .serializers import StockSerializer

class StockListCreateAPIView(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer