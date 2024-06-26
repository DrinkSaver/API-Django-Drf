from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Créez une vue de schéma Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="DrinkSaver API",  # Titre de votre API
        default_version="v1",  # Version par défaut de l'API
        description="API  for ApiDrinkSaver",  # Description de l'API
        terms_of_service="https://www.example.com/terms/",  # Conditions d'utilisation de l'API
        contact=openapi.Contact(email="contact@example.com"),  # Contact pour l'API
        license=openapi.License(name="Example License"),  # Licence de l'API
    ),
    public=True,  # Autorise l'accès public à la documentation Swagger
    permission_classes=(permissions.AllowAny,),  # Autorise tous les utilisateurs à accéder à la documentation
)

urlpatterns = [
    path("admin/", admin.site.urls),  # URL de l'interface d'administration de Django

    # URL de l'API
    path("api/", include('ApiDrinkSaver.urls')),

    # Définition des URL pour Swagger (avec vérification DEBUG)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
