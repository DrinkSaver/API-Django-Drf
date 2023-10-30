from django.db import models
from django.db.models import Q
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.sites.models import Site

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from allauth.account.utils import complete_signup
from allauth.account.models import EmailAddress
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.oauth2.client import OAuth2Error

from ApiDrinkSaver.models.user import User
from ApiDrinkSaver.serializers.user_serializer import CustomUserSerializer, UserProfileSerializer
from ApiDrinkSaver.permissions import IsOwnerOrAdmin


class CustomEmailAddress(EmailAddress):
    custom_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)


class CustomAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        msg.send()

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = Site.objects.get_current(request)
        key = emailconfirmation.key
        activate_url = reverse(
            "account:confirm_email",
            args=[key]
        )
        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": "{0}{1}".format(current_site.domain, activate_url),
            "email": emailconfirmation.email_address.email,
            "key": key,
        }
        self.send_mail("account/confirmation_signup_message", emailconfirmation.email_address.email, ctx)


@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def register_user(request):
    """
    Cette vue permet à un utilisateur lambda de s'inscrire par e-mail ou par des comptes de médias sociaux.
    """
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if username and email and password:
        user, created = User.objects.get_or_create(email=email)
        if created:
            user.username = username  # Ajoute le nom d'utilisateur
            user.set_password(password)
            user.save()

        email_address, email_created = CustomEmailAddress.objects.get_or_create(user=user, email=email)
        if email_created:
            email_address.verified = False
            email_address.primary = True
            email_address.save()

            user.send_email_confirmation()

            return JsonResponse({"detail": _("L'inscription a réussi. Un e-mail de confirmation a été envoyé.")})
        else:
            return JsonResponse({"detail": _("Cet e-mail est déjà associé à un compte.")}, status=400)

    social_provider = request.data.get("social_provider")
    social_token = request.data.get("social_token")
    if social_provider and social_token:
        try:
            account = SocialAccount.get_social_account(social_provider, social_token)
            if account and account.user:
                return JsonResponse({"detail": _("Cet utilisateur social existe déjà.")}, status=400)
            user = User.objects.create(email=email)
            account = SocialAccount(user=user, uid=social_token, provider=social_provider)
            account.save()
            complete_signup(request, user, EmailConfirmation.objects.filter(email=email).first())
            return JsonResponse({"detail": _("L'inscription a réussi.")})
        except OAuth2Error:
            return JsonResponse({"detail": _("Echec de l'inscription via le compte social.")}, status=400)

    return JsonResponse({"detail": _("Données d'inscription invalides.")})


@api_view(['POST'])
def verify_email(request):
    """
    Cette vue permet à un utilisateur de confirmer son adresse e-mail en utilisant le code de confirmation reçu par e-mail.
    """
    email = request.data.get("email")
    confirmation_code = request.data.get("confirmation_code")

    if email and confirmation_code:
        email_address = CustomEmailAddress.objects.get(email=email)
        if email_address and email_address.confirmation_key == confirmation_code and not email_address.verified:
            email_address.verified = True
            email_address.save()
            return JsonResponse({'detail': _("Adresse e-mail vérifiée avec succès.")})
        return JsonResponse({"detail": _("Code de confirmation invalide ou adresse e-mail déjà vérifiée.")}, status=400)
    return JsonResponse({"detail": _("Données invalides.")}, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    """
    Cette vue permet à tout le monde de se connecter
    """
    return obtain_auth_token(request)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_all_users():
    """
    Cette vue permet à l'administrateur de récupérer la liste de tous les utilisateurs.
    """
    users = User.objects.all()
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
    try:
        user = User.objects.get(id=user_id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"detail": _("Utilisateur non trouvé.")}, status=status.HTTP_404_NOT_FOUND)


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
        users = User.objects.filter(
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
    users = User.objects.all()
    paginator = LimitOffsetPagination()
    paginated_users = paginator.paginate_queryset(users, request)
    serializer = CustomUserSerializer(paginated_users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrAdmin]
