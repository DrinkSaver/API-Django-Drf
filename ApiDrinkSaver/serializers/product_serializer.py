from rest_framework import serializers
from ApiDrinkSaver.models.product_bar import Product, Bar, BarProductPrice


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = '__all__'


class BarProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarProductPrice
        fields = '__all__'
