from rest_framework import generics, permissions
from ApiDrinkSaver.models.bar import Bar
from ApiDrinkSaver.serializers.bar_serializer import BarSerializer


class BarCreateView(generics.CreateAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = [permissions.IsAuthenticated]


class BarListView(generics.ListAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = [permissions.AllowAny]


class BarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
