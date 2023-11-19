from rest_framework import generics
from ApiDrinkSaver.models.categoryDrink import CategoryDrink
from ApiDrinkSaver.serializers.categoryDrink_serializer import CategoryDrinkSerializer


class CategoryDrinkListView(generics.ListAPIView):
    queryset = CategoryDrink.objects.all()
    serializer_class = CategoryDrinkSerializer
