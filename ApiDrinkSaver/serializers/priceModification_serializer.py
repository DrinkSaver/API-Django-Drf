from rest_framework import serializers
from ApiDrinkSaver.models.priceModification import PriceModification


class PriceModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceModification
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(PriceModificationSerializer, self).to_representation(instance)
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        # Vérifier si l'utilisateur est un utilisateur lambda
        if user.is_lambda:
            price_modification = PriceModification.objects.create(**validated_data)
            price_modification.votes.add(user)
            # Ajouter automatiquement le vote de l'utilisateur qui a créé la modification
            return price_modification

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user

        # Vérifier si l'utilisateur est un utilisateur lambda
        if user.is_lambda:
            # Si l'utilisateur n'a pas déjà voté, ajouter son vote
            if user not in instance.votes.all():
                instance.votes.add(user)

            # Mettre à jour les autres champs de la modification de prix
            for attr, value in validated_data.items():
                setattr(instance, attr, value)

            instance.save()
            return instance

    def delete(self, instance):
        request = self.context.get('request')
        user = request.user

        # Vérifier si l'utilisateur est un utilisateur lambda
        if user.is_lambda:
            instance.delete()
