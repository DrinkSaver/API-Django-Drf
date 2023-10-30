from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.contrib.sites.models import Site
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from allauth.socialaccount.models import SocialAccount
from django.utils.translation import gettext_lazy as _


# Créez un gestionnaire de modèle personnalisé pour le modèle CustomUser
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("L'adresse e-mail doit être spécifiée"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


# Créez un modèle utilisateur personnalisé en utilisant AbstractBaseUser
class User(AbstractBaseUser, PermissionsMixin):
    # Champs de base pour l'authentification
    username = models.CharField(max_length=30, unique=True, verbose_name=_("Nom d'utilisateur"), default="")
    email = models.EmailField(unique=True, verbose_name=_("Adresse e-mail"))
    email_verified = models.BooleanField(default=False, verbose_name=_("Adresse e-mail vérifiée"))
    password = models.CharField(max_length=128, verbose_name=_("Mot de passe"))

    # Champs spécifiques à l'utilisateur
    first_name = models.CharField(max_length=30, verbose_name="Prénom")
    last_name = models.CharField(max_length=30, verbose_name="Nom de famille")

    # Champs pour gérer le type d'utilisateur
    is_staff = models.BooleanField(default=False, verbose_name="Administrateur")
    is_bar_owner = models.BooleanField(default=False, verbose_name="Propriétaire de bar")
    is_lambda_user = models.BooleanField(default=True, verbose_name="Utilisateur standard")

    # Champs pour les informations de profil
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date de naissance")
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True,
                                      verbose_name="Photo de profil")
    bio = models.TextField(max_length=500, blank=True, verbose_name="Biographie")
    location = models.CharField(max_length=100, blank=True, verbose_name="Emplacement")

    # Champs spécifiques aux propriétaires de bar
    bar_name = models.CharField(max_length=100, verbose_name="Nom du bar")
    address = models.CharField(max_length=200, verbose_name="Adresse du bar")

    # Champs spécifiques related_name personnalisés pour éviter les conflits
    groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name="custom_users")
    user_permissions = models.ManyToManyField(Permission, verbose_name="User permissions", blank=True,
                                              related_name="custom_users")
    # Champs pour les comptes de médias sociaux
    linked_social_accounts = models.ManyToManyField(SocialAccount, related_name="users", blank=True,
                                                    verbose_name="Comptes de médias sociaux liés")

    # Utilisez un gestionnaire personnalisé
    objects = CustomUserManager()

    # Utilisez l'adresse e-mail comme champ de connexion
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Utilisateur personnalisé")
        verbose_name_plural = _("Utilisateurs personnalisés")

    def send_email_confirmation(self):
        email_address, created = EmailAddress.objects.get_or_create(user=self, email=self.email, verified=False)
        if created:
            send_email_confirmation(self, email_address)


# Créez un modèle pour le profil de l'utilisateur
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",
                                verbose_name="Utilisateur")

    # Ajoutez davantage de champs spécifiques au profil utilisateur
    interests = models.CharField(max_length=100, blank=True, verbose_name="Centres d'intérêt")
    website = models.URLField(max_length=200, blank=True, verbose_name="Site Web personnel")

    class Meta:
        verbose_name = "Profil d'utilisateur"
        verbose_name_plural = "Profils d'utilisateurs"


# Créez un modèle pour le profil du propriétaire de bar
class BarOwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="bar_owner",
                                verbose_name="Propriétaire de bar")

    # Ajoutez davantage de champs spécifiques au profil du propriétaire de bar
    bar_description = models.TextField(max_length=500, blank=True, verbose_name="Description du bar")
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="Numéro de téléphone")

    class Meta:
        verbose_name = "Profil du propriétaire de bar"
        verbose_name_plural = "Profils des propriétaires de bar"
