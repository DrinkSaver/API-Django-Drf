from rest_framework import serializers
from ApiDrinkSaver.models.user import User, UserProfile, BarOwnerProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class BarOwnerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarOwnerProfile
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    bar_owner = BarOwnerProfileSerializer()

    class Meta:
        model = User
        fields = "__all__"
