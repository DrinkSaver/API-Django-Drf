from rest_framework import serializers
from ApiDrinkSaver.models import UserLambda, PriceModification, Drink
from django.contrib.auth.hashers import make_password


class UserLambdaSerializer(serializers.ModelSerializer):
    """
    Serializer for UserLambda model.
    """
    class Meta:
        model = UserLambda
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'date_of_birth',
            'profile_picture',
            'favorite_drinks',
            'drink_price_modifications',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

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


class UserLambdaPasswordUpdateSerializer(serializers.Serializer):
    """
    Serializer for updating the password of a UserLambda object.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
