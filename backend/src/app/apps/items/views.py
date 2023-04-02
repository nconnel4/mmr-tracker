from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer


class ItemList(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
