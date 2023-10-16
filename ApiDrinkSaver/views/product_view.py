from rest_framework import generics
from ApiDrinkSaver.models.product import Product, Bar, BarProductPrice
from ApiDrinkSaver.serializers.product_serializer import ProductSerializer, BarSerializer, BarProductPriceSerializer
from ApiDrinkSaver.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsLambdaOrReadOnly, IsLambdaCanModifyPrice, \
    IsOwnerCanModifyBar


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class BarList(generics.ListCreateAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = [IsAdminOrReadOnly]


class BarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = [IsOwnerOrReadOnly]


class BarProductPriceList(generics.ListCreateAPIView):
    queryset = BarProductPrice.objects.all()
    serializer_class = BarProductPriceSerializer
    permission_classes = [IsLambdaOrReadOnly]


class BarProductPriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BarProductPrice.objects.all()
    serializer_class = BarProductPriceSerializer
    permission_classes = [IsLambdaCanModifyPrice, IsOwnerOrReadOnly]
