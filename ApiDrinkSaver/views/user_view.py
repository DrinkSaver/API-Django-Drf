from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from allauth.account.views import SignupView, LoginView

# Exemples de vues pour l'inscription, la connexion, etc.
@api_view(["POST"])
def custom_user_signup(request):
# Vue personnalisée pour l'inscription
    # Utilisez SignupView de Django-Allauth ou personnalisez la vôtre.

@api_view(["POST"])
def custom_user_login(request):
# Vue personnalisée pour la connexion
    # Utilisez LoginView de Django-Allauth ou personnalisez la vôtre.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):
# Vue pour afficher le profil de l'utilisateur actuellement connecté
    # Vous pouvez personnaliser cela pour afficher des informations spécifiques au type d'utilisateur.
