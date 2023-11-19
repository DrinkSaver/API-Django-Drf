from rest_framework import serializers
from ApiDrinkSaver.models.drinkPrice import DrinkPrice


class DrinkPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkPrice
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(DrinkPriceSerializer, self).to_representation(instance)
        return representation
