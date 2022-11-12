
from django.urls import path
from .views import OptionListCreateAPIView, OptionRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('api/v1/option/', OptionListCreateAPIView.as_view(),name='option'),
    path('api/v1/option/<int:pk>', OptionRetrieveUpdateDestroyAPIView.as_view(),name='option'),
]