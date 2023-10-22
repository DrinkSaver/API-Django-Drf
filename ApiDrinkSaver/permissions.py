from django.contrib.auth.models import Permission
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_staff


class IsLambdaUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_lambda_user


class CanModifyBarPrice(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            # Vérifier si l'utilisateur est un utilisateur lambda
            if request.user.is_lambda_user:
                # Vérifier si l'utilisateur a déjà soumis 4 modifications pour le même produit de bar
                total_lambda_changes = UserModifiedBarPrice.objects.filter(
                    bar=obj.bar, product=obj.product, user=request.user).count()
                return total_lambda_changes < 4
            return False
        return True
