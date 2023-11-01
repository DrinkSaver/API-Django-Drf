from rest_framework.exceptions import ValidationError
from rest_framework import generics
from ApiDrinkSaver.modules.pagination import CustomPagination
from ApiDrinkSaver.serializers.favorites_serializer import FavoriteItemSerializer
from ApiDrinkSaver.models.favorites import FavoriteItem


class FavoriteItemList(generics.ListAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer
    pagination_class = CustomPagination


class FavoriteItemCreateView(generics.CreateAPIView):
    serializer_class = FavoriteItemSerializer

    def perform_create(self, serializer):
        item = serializer.validated_data.get('item')
        if not item:
            raise ValidationError("L'élément favori n'existe pas.")
        serializer.save()
