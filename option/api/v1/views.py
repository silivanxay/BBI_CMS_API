from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from option.models import Option
from .serializers import OptionSerializer

class OptionListCreateAPIView(ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
