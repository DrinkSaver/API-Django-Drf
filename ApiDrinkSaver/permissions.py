from rest_framework import permissions
from ApiDrinkSaver.models.product import UserModifiedBarPrice


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsLambdaOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_type == 'lambda'


class IsLambdaCanModifyPrice(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            total_lambda_changes = UserModifiedBarPrice.objects.filter(
                bar=obj.bar, product=obj.product, user=request.user).count()
            return request.user.user_type == 'lambda' and total_lambda_changes >= 4
        return True


class IsOwnerCanModifyBar(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
