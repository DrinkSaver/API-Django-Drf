from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ApiDrinkSaver.models.favorites import FavoriteItem
from ApiDrinkSaver.serializers.favorites_serializer import FavoriteItemSerializer
from rest_framework.exceptions import PermissionDenied


class FavoriteItemListCreateView(generics.ListCreateAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Vérifiez si l'utilisateur est un utilisateur lambda
        if self.request.user.is_lambda:
            serializer.save(user=self.request.user)
        else:
            raise PermissionDenied("Vous n'avez pas la permission de créer un favori.")


class FavoriteItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Vérifiez si l'utilisateur est un utilisateur lambda
        if self.request.user.is_lambda:
            serializer.save()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de mettre à jour ce favori.")

    def perform_destroy(self, instance):
        # Vérifiez si l'utilisateur est un utilisateur lambda
        if self.request.user.is_lambda:
            instance.delete()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de supprimer ce favori.")
