# serializers/bar_serializer.py
from rest_framework import serializers
from ApiDrinkSaver.models.bar import Bar
from ApiDrinkSaver.models.barFilter import BarFilter
from ApiDrinkSaver.serializers.barFilter_serializer import BarFilterSerializer


class BarSerializer(serializers.ModelSerializer):
    filters = BarFilterSerializer()

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

        filters_data = validated_data.pop('filters', {})
        bar = Bar.objects.create(**validated_data)
        BarFilter.objects.create(bar=bar, **filters_data)

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

        filters_data = validated_data.pop('filters', {})
        filters_instance = instance.filters

        instance.name = validated_data.get('name', instance.name)
        # ... (autres champs de Bar)

        for attr, value in filters_data.items():
            setattr(filters_instance, attr, value)
        filters_instance.save()

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
