from rest_framework import serializers
from ApiDrinkSaver.models.categoryDrink import CategoryDrink


class CategoryDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDrink
        fields = '__all__'
