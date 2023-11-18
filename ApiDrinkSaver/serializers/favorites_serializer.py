from rest_framework import serializers
from ApiDrinkSaver.models.bar import Bar
from ApiDrinkSaver.models.drink import Drink
from ApiDrinkSaver.models.favorites import FavoriteItem
from ApiDrinkSaver.serializers.drink_serializer import DrinkSerializer
from ApiDrinkSaver.serializers.bar_serializer import BarSerializer


class FavoriteItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = FavoriteItem
        fields = ('id', 'user', 'item_type', 'item_id', 'item')

    def get_item(self, obj):
        if obj.item_type == 'drink':
            try:
                drink = Drink.objects.get(id=obj.item_id)
                serializer = DrinkSerializer(drink)
                return serializer.data
            except Drink.DoesNotExist:
                return None
        elif obj.item_type == 'bar':
            try:
                bar = Bar.objects.get(id=obj.item_id)
                serializer = BarSerializer(bar)
                return serializer.data
            except Bar.DoesNotExist:
                return None
        return None
