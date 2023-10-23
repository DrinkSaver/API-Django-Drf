from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from ApiDrinkSaver.views.user_view import (
    get_all_users, get_user_profile, get_user_by_id, update_user_profile, search_users,
    get_paginated_users, UserProfileViewSet, register_user, verify_email
)
from rest_framework.authtoken.views import obtain_auth_token

# Utilisez DefaultRouter pour gérer les vues avec ModelViewSet
router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('users/', get_all_users, name='get_all_users'),
    path('user/profile/', get_user_profile, name='get_user_profile'),
    path('user/profile/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('user/profile/update/', update_user_profile, name='update_user_profile'),
    path('user/search/', search_users, name='search_users'),
    path('users/paginated/', get_paginated_users, name='get_paginated_users'),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', register_user, name='register_user'),  # Ajoutez cette ligne
    path('verify-email/', verify_email, name='verify_email'),  # Ajoutez cette ligne
    path('', include(router.urls)),
]
