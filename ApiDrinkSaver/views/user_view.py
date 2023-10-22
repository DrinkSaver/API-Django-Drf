from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from ApiDrinkSaver.models.user import CustomUser
from ApiDrinkSaver.serializers.user_serializer import CustomUserSerializer, UserProfileSerializer
from ApiDrinkSaver.permissions import IsOwnerOrAdmin


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_all_users(request):
    """
    Cette vue permet à l'administrateur de récupérer la liste de tous les utilisateurs.
    """
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """
    Cette vue permet à un utilisateur authentifié de récupérer son propre profil.
    """
    user = request.user
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwnerOrAdmin])
def get_user_by_id(request, user_id):
    """
    Cette vue permet à un utilisateur authentifié ou à un administrateur de récupérer le profil d'un utilisateur par son ID.
    """
    user = get_object_or_404(CustomUser, id=user_id)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    """
    Cette vue permet à un utilisateur authentifié de mettre à jour son propre profil.
    """
    user = request.user
    serializer = CustomUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_users(request):
    """
    Cette vue permet à un utilisateur authentifié de rechercher d'autres utilisateurs par nom, prénom ou adresse e-mail.
    """
    query = request.query_params.get('q')
    if query:
        users = CustomUser.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)
        )
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response([])


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_paginated_users(request):
    """
    Cette vue permet à l'administrateur de récupérer une liste paginée de tous les utilisateurs.
    """
    users = CustomUser.objects.all()
    paginator = LimitOffsetPagination()
    paginated_users = paginator.paginate_queryset(users, request)
    serializer = CustomUserSerializer(paginated_users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrAdmin]
