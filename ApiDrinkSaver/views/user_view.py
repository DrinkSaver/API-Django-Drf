from django.core.mail import send_mail
from rest_framework import permissions, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from ApiDrinkSaver.models.user import CustomUser
from ApiDrinkSaver.serializers.user_serializer import CustomUserCreateSerializer, CustomUserSerializer


class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CustomUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False  # Désactivation du compte jusqu'à ce qu'il soit vérifié par e-mail

            # Génération d'un code de confirmation (par exemple, un code à 6 chiffres)
            confirmation_code = generate_confirmation_code()

            # Enregistrement du code de confirmation dans la base de données avec l'utilisateur
            user.confirmation_code = confirmation_code
            user.save()

            # Envoi de l'e-mail de confirmation à l'utilisateur
            send_confirmation_email(user.email, confirmation_code)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Fonction pour envoyer un e-mail de confirmation
def send_confirmation_email(email, confirmation_code):
    subject = 'Confirmation de votre compte'
    message = f'Votre code de confirmation est : {confirmation_code}'
    from_email = 'votre@adresse.email'  # Remplacer par une adresse e-mail d'envoi
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


# Fonction pour générer un code de confirmation
def generate_confirmation_code():
    import random
    return ''.join(random.choice('0123456789') for _ in range(6))


class UserLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Retournez l'objet utilisateur actuellement authentifié
        return self.request.user


# Vue pour la réinitialisation du mot de passe
class PasswordResetView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')

        # Vérifier l'existence de l'e-mail dans la base de données
        user = CustomUser.objects.filter(email=email).first()

        if user:
            # Génération d'un code de réinitialisation (par exemple, un code à 6 chiffres)
            reset_code = generate_reset_code()

            # Enregistrement du code de réinitialisation dans la base de données avec l'utilisateur
            user.reset_code = reset_code
            user.save()

            # Envoi de l'e-mail de réinitialisation à l'utilisateur
            send_reset_email(user.email, reset_code)

            return Response({'detail': 'Un e-mail de réinitialisation a été envoyé'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Aucun utilisateur n\'est associé à cet e-mail'},
                            status=status.HTTP_404_NOT_FOUND)


# Fonction pour générer un code de réinitialisation
def generate_reset_code():
    import random
    return ''.join(random.choice('0123456789') for _ in range(6))


# Fonction pour envoyer un e-mail de réinitialisation
def send_reset_email(email, reset_code):
    subject = 'Réinitialisation du mot de passe'
    message = f'Votre code de réinitialisation est : {reset_code}'
    from_email = 'votre@adresse.email'  # Remplacer par une adresse e-mail d'envoi
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


# Vue pour la confirmation de réinitialisation de mot de passe
class PasswordResetConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        reset_code = request.data.get('reset_code')

        # Vérifier si le code de réinitialisation est valide pour l'utilisateur
        user = CustomUser.objects.filter(email=email, reset_code=reset_code).first()

        if user:
            new_password = generate_random_password()

            # Réinitialisation du mot de passe
            user.set_password(new_password)
            user.reset_code = None
            user.save()

            # Envoi du nouveau mot de passe à l'utilisateur
            send_new_password_email(user.email, new_password)

            return Response({'detail': 'Le mot de passe a été réinitialisé avec succès'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Code de réinitialisation invalide'}, status=status.HTTP_400_BAD_REQUEST)


# Fonction pour générer un nouveau mot de passe aléatoire
def generate_random_password():
    import random
    import string
    password_length = 12
    characters = string.ascii_letters + string.digits
    new_password = ''.join(random.choice(characters) for i in range(password_length))
    return new_password


# Fonction pour envoyer le nouveau mot de passe par e-mail
def send_new_password_email(email, new_password):
    subject = 'Nouveau mot de passe'
    message = f'Votre nouveau mot de passe est : {new_password}'
    from_email = 'votre@adresse.email'  # Remplacer par une adresse e-mail d'envoi
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
