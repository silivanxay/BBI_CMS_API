
from django.urls import path
from .views import StockListCreateAPIView, StockRetrieveUpdateDestroyAPIView,  OptionListCreateAPIView, OptionRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/stock/', StockListCreateAPIView.as_view(),name='stock'),
    path('api/v1/stock/<int:pk>', StockRetrieveUpdateDestroyAPIView.as_view(),name='stock'),
    path('api/v1/option/', OptionListCreateAPIView.as_view(),name='option'),
    path('api/v1/option/<int:pk>', OptionRetrieveUpdateDestroyAPIView.as_view(),name='option'),
]