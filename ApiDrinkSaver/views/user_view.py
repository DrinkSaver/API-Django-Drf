from rest_framework import viewsets, permissions
from ApiDrinkSaver.models.user import CustomUser, UserProfile, BarOwnerProfile
from ApiDrinkSaver.serializers.user_serializer import (CustomUserSerializer, UserProfileSerializer,
                                                       BarOwnerProfileSerializer)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class BarOwnerProfileViewSet(viewsets.ModelViewSet):
    queryset = BarOwnerProfile.objects.all()
    serializer_class = BarOwnerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
