from rest_framework import serializers
from ApiDrinkSaver.models.barFilter import BarFilter


class BarFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarFilter
        fields = '__all__'
