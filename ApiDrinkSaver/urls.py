# Dans votre fichier urls.py de l'application

from django.urls import path
from . import views

urlpatterns = [
    # Ajoutez ici vos différentes vues et leurs chemins d'URL
    path('api/drinks/', views.DrinkListView.as_view(), name='drink-list'),
    path('api/drinks/<int:pk>/', views.DrinkDetailView.as_view(), name='drink-detail'),
    path('api/bars/', views.BarListView.as_view(), name='bar-list'),
    path('api/bars/<int:pk>/', views.BarDetailView.as_view(), name='bar-detail'),
    path('api/users/', views.UserLambdaListView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', views.UserLambdaDetailView.as_view(), name='user-detail'),
    # ... Ajoutez d'autres chemins d'URL ici ...
]
