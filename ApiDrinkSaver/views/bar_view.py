from rest_framework.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ApiDrinkSaver.models.bar import Bar
from ApiDrinkSaver.serializers.bar_serializer import BarSerializer


class BarListCreateView(generics.ListCreateAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assignez le propriétaire du bar actuel à l'utilisateur authentifié
        serializer.save(owner=self.request.user)


class BarRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Vérifiez si l'utilisateur est propriétaire du bar ou un administrateur
        if self.request.user == serializer.instance.owner or self.request.user.is_staff:
            serializer.save()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de mettre à jour ce bar.")

    def perform_destroy(self, instance):
        # Vérifiez si l'utilisateur est propriétaire du bar ou un administrateur
        if self.request.user == instance.owner or self.request.user.is_staff:
            instance.delete()
        else:
            raise PermissionDenied("Vous n'avez pas la permission de supprimer ce bar.")
