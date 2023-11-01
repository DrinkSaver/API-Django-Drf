from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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

    def get_favorite_drinks(self, obj):
        """
        Récupérer les boissons favorites de l'utilisateur.
        """
        favorite_drinks = obj.favorite_drinks.all()
        return FavoriteDrinkSerializer(favorite_drinks, many=True).data

    def delete_favorite_drink(self, obj, validated_data):
        """
        Supprimer une boisson des favoris de l'utilisateur.
        """
        drink_id = validated_data.get('drink_id')
        favorite_drink = obj.favorite_drinks.filter(drink_id=drink_id).first()
        if favorite_drink:
            favorite_drink.delete()


class UserLambdaPasswordUpdateSerializer(serializers.Serializer):
    """
    Serializer for updating the password of a UserLambda object.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
