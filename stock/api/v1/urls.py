
from django.urls import path
from .views import StockListCreateAPIView, StockRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/stock/', StockListCreateAPIView.as_view(),name='stock'),
    path('api/v1/stock/<int:pk>', StockRetrieveUpdateDestroyAPIView.as_view(),name='stock'),
]