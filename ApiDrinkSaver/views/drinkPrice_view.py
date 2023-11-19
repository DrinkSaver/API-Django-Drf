from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ApiDrinkSaver.models.drinkPrice import DrinkPrice
from ApiDrinkSaver.serializers.drinkPrice_serializer import DrinkPriceSerializer
from rest_framework.exceptions import PermissionDenied


class DrinkPriceListCreateView(generics.ListCreateAPIView):
    queryset = DrinkPrice.objects.all()
    serializer_class = DrinkPriceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Vérifiez si l'utilisateur est propriétaire du bar ou un administrateur
        if self.request.user.is_bar or self.request.user.is_staff:
            serializer.save()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de créer un prix de boisson.")


class DrinkPriceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DrinkPrice.objects.all()
    serializer_class = DrinkPriceSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Vérifiez si l'utilisateur est propriétaire du bar ou un administrateur
        if self.request.user.is_bar or self.request.user.is_staff:
            serializer.save()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de mettre à jour ce prix de boisson.")

    def perform_destroy(self, instance):
        # Vérifiez si l'utilisateur est propriétaire du bar ou un administrateur
        if self.request.user.is_bar or self.request.user.is_staff:
            instance.delete()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de supprimer ce prix de boisson.")
