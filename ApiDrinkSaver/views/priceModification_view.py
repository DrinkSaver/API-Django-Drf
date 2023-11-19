from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ApiDrinkSaver.models.priceModification import PriceModification
from ApiDrinkSaver.serializers.priceModification_serializer import PriceModificationSerializer
from rest_framework.exceptions import PermissionDenied


class PriceModificationListCreateView(generics.ListCreateAPIView):
    queryset = PriceModification.objects.all()
    serializer_class = PriceModificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Vérifiez si l'utilisateur est un utilisateur lambda
        if self.request.user.is_lambda:
            serializer.save(user=self.request.user)
        else:
            raise PermissionDenied("Vous n'avez pas la permission de créer une modification de prix.")


class PriceModificationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceModification.objects.all()
    serializer_class = PriceModificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Vérifiez si l'utilisateur est un utilisateur lambda
        if self.request.user.is_lambda:
            serializer.save()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de mettre à jour cette modification de prix.")

    def perform_destroy(self, instance):
        # Vérifiez si l'utilisateur est un utilisateur lambda
        if self.request.user.is_lambda:
            instance.delete()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de supprimer cette modification de prix.")
