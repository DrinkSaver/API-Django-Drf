from rest_framework import viewsets, permissions
from ApiDrinkSaver.models.product import Product
from ApiDrinkSaver.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.user.user_type == 'admin':
            # Les administrateurs ont toutes les autorisations
            return [permissions.AllowAny()]
        elif self.request.user.user_type in ['lambda', 'owner']:
            # Les utilisateurs lambda et propriétaires ont la permission de lecture uniquement
            return [permissions.IsAuthenticated(), permissions.ReadOnly]
