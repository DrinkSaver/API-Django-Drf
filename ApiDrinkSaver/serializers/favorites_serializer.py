from rest_framework import serializers
from ApiDrinkSaver.models.favorites import FavoriteDrink, FavoriteBar


class FavoriteDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteDrink
        fields = '__all__'
        extra_kwargs = {
            'user': {'write_only': True},
        }


class FavoriteBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteBar
        fields = '__all__'
        extra_kwargs = {
            'user': {'write_only': True},
        }