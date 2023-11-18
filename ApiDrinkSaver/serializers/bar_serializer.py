from rest_framework import serializers
from ApiDrinkSaver.models.bar import Bar


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(BarSerializer, self).to_representation(instance)
        # Personnalisez la représentation si nécessaire
        return representation

    def create(self, validated_data):
        """
        Crée un nouvel objet Bar (réservé aux administrateurs et aux bars).
        """
        request = self.context.get('request')
        user = request.user

        # Vérifiez si l'utilisateur est administrateur ou bar
        if not (user.is_staff or user.is_bar):
            raise serializers.ValidationError("Vous n'avez pas l'autorisation de créer un bar.")

        bar = Bar.objects.create(**validated_data)
        return bar

    def update(self, instance, validated_data):
        """
        Met à jour un objet Bar (réservé aux administrateurs et aux bars).
        """
        request = self.context.get('request')
        user = request.user

        # Vérifiez si l'utilisateur est administrateur ou bar
        if not (user.is_staff or user.is_bar):
            raise serializers.ValidationError("Vous n'avez pas l'autorisation de mettre à jour ce bar.")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        """
        Supprime un objet Bar (réservé aux administrateurs et aux bars).
        """
        request = self.context.get('request')
        user = request.user

        # Vérifiez si l'utilisateur est administrateur ou bar
        if not (user.is_staff or user.is_bar):
            raise serializers.ValidationError("Vous n'avez pas l'autorisation de supprimer ce bar.")

        instance.delete()
