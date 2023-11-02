from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from ApiDrinkSaver.models.userLambda import UserLambda
from ApiDrinkSaver.models.priceModification import PriceModification
from ApiDrinkSaver.models.drink import Drink


class UserLambdaSerializer(serializers.ModelSerializer):
    """
    Serializer for UserLambda model.
    """

    class Meta:
        model = UserLambda
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        """
        Validate the password and hash it before saving.
        """
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return make_password(value)

    def create(self, validated_data):
        """
        Method called when creating a new UserLambda object (registration).
        """
        password = make_password(validated_data['password'])
        user = UserLambda.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )

        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.date_of_birth = validated_data.get('date_of_birth', user.date_of_birth)
        user.profile_picture = validated_data.get('profile_picture', user.profile_picture)

        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Method called when updating an existing UserLambda object.
        """
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserLambdaSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        """
        Serialize the UserLambda object.
        """
        data = super(UserLambdaSerializer, self).to_representation(instance)
        # Add any additional data or custom fields you want to include
        data['custom_field'] = instance.custom_field
        return data


class UserLambdaPasswordUpdateSerializer(serializers.Serializer):
    """
    Serializer for updating the password of a UserLambda object.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
