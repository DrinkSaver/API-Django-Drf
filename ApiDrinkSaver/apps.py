from django.apps import AppConfig


class ApidrinksaverConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ApiDrinkSaver"


class SocialAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'allauth.socialaccount'
    label = 'allauth.socialaccount'
