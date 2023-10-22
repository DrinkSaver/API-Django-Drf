from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user/profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('user/search/', views.UserSearchView.as_view(), name='user-search'),
    # Autres URL pour la gestion des utilisateurs
]
