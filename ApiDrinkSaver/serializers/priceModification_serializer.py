from rest_framework import serializers
from ApiDrinkSaver.models.priceModification import PriceModification
from ApiDrinkSaver.models.bar import Bar


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
            # Vérifier s'il y a une modification déjà soumise par l'utilisateur pour la même boisson
            existing_modification = PriceModification.objects.filter(
                user=user,
                drink=validated_data['drink'],
                status='PENDING'
            ).first()

            if existing_modification:
                raise serializers.ValidationError(
                    "Vous avez déjà soumis une modification en attente pour cette boisson.")

            # Créer la modification de prix
            price_modification = PriceModification.objects.create(**validated_data)
            price_modification.votes.add(user)
            return price_modification

        # Vérifier si l'utilisateur est un propriétaire de bar
        elif user.is_bar:
            # Vérifier si le bar associé à la modification est le bar de l'utilisateur
            bar = Bar.objects.get(pk=validated_data['bar'].pk)
            if bar.owner != user:
                raise serializers.ValidationError("Vous n'avez pas l'autorisation de modifier les prix pour ce bar.")

            # Créer la modification de prix
            price_modification = PriceModification.objects.create(**validated_data)
            price_modification.is_approved = True  # Approuver automatiquement la modification pour le propriétaire de bar
            price_modification.save()
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

        # Vérifier si l'utilisateur est un propriétaire de bar
        elif user.is_bar:
            raise serializers.ValidationError("Vous n'avez pas l'autorisation de modifier les prix pour ce bar.")

    def delete(self, instance):
        request = self.context.get('request')
        user = request.user

        # Vérifier si l'utilisateur est un utilisateur lambda
        if user.is_lambda:
            instance.delete()

        # Vérifier si l'utilisateur est un propriétaire de bar
        elif user.is_bar:
            raise serializers.ValidationError("Vous n'avez pas l'autorisation de supprimer cette modification de prix.")
