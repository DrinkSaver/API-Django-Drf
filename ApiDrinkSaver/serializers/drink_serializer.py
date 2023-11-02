from rest_framework import serializers
from ApiDrinkSaver.models.drink import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(DrinkSerializer, self).to_representation(instance)
        return representation

    def create(self, validated_data):
        """
        Crée un nouvel objet Drink (réservé aux administrateurs et aux bars).
        """
        request = self.context.get('request')
        user = request.user

        # Vérifiez si l'utilisateur est administrateur ou bar
        if user.is_staff or user.is_bar:
            drink = Drink.objects.create(**validated_data)
            return drink

    def update(self, instance, validated_data):
        """
        Met à jour un objet Drink (réservé aux administrateurs et aux bars).
        """
        request = self.context.get('request')
        user = request.user

        # Vérifiez si l'utilisateur est administrateur ou bar
        if user.is_staff or user.is_bar:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            return instance

    def delete(self, instance):
        """
        Supprime un objet Drink (réservé aux administrateurs et aux bars).
        """
        request = self.context.get('request')
        user = request.user

        # Vérifiez si l'utilisateur est administrateur ou bar
        if user.is_staff or user.is_bar:
            instance.delete()
