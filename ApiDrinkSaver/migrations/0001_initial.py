# Generated by Django 4.2.6 on 2023-10-22 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("socialaccount", "0005_socialtoken_nullable_app"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=30, unique=True, verbose_name="Surnom"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Adresse e-mail"
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="Mot de passe"),
                ),
                ("first_name", models.CharField(max_length=30, verbose_name="Prénom")),
                (
                    "last_name",
                    models.CharField(max_length=30, verbose_name="Nom de famille"),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Administrateur"),
                ),
                (
                    "is_bar_owner",
                    models.BooleanField(
                        default=False, verbose_name="Propriétaire de bar"
                    ),
                ),
                (
                    "is_lambda_user",
                    models.BooleanField(
                        default=True, verbose_name="Utilisateur standard"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date de naissance"
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_images/",
                        verbose_name="Photo de profil",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="Biographie"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Emplacement"
                    ),
                ),
                (
                    "bar_name",
                    models.CharField(max_length=100, verbose_name="Nom du bar"),
                ),
                (
                    "address",
                    models.CharField(max_length=200, verbose_name="Adresse du bar"),
                ),
                (
                    "linked_social_accounts",
                    models.ManyToManyField(
                        blank=True,
                        related_name="users",
                        to="socialaccount.socialaccount",
                        verbose_name="Comptes de médias sociaux liés",
                    ),
                ),
            ],
            options={
                "verbose_name": "Utilisateur personnalisé",
                "verbose_name_plural": "Utilisateurs personnalisés",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "interests",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Centres d'intérêt"
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, verbose_name="Site Web personnel"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to="ApiDrinkSaver.customuser",
                        verbose_name="Utilisateur",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profil d'utilisateur",
                "verbose_name_plural": "Profils d'utilisateurs",
            },
        ),
        migrations.CreateModel(
            name="BarOwnerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bar_description",
                    models.TextField(
                        blank=True, max_length=500, verbose_name="Description du bar"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="Numéro de téléphone"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bar_owner",
                        to="ApiDrinkSaver.customuser",
                        verbose_name="Propriétaire de bar",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profil du propriétaire de bar",
                "verbose_name_plural": "Profils des propriétaires de bar",
            },
        ),
    ]