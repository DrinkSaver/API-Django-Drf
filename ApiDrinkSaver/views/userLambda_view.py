from rest_framework import generics
from ApiDrinkSaver.models.userLambda import UserLambda
from ApiDrinkSaver.serializers.userLambda_serializer import UserLambdaSerializer
from rest_framework.permissions import IsAuthenticated


class UserLambdaListView(generics.ListCreateAPIView):
    queryset = UserLambda.objects.all()
    serializer_class = UserLambdaSerializer
    permission_classes = [IsAuthenticated]


class UserLambdaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserLambda.objects.all()
    serializer_class = UserLambdaSerializer
    permission_classes = [IsAuthenticated]
