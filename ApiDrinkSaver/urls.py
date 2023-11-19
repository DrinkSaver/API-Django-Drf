from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from ApiDrinkSaver.views.userLambda_view import UserLambdaListView, UserLambdaDetailView
from ApiDrinkSaver.views.bar_view import BarListCreateView, BarRetrieveUpdateDeleteView
from ApiDrinkSaver.views.drinkPrice_view import DrinkPriceListCreateView, DrinkPriceRetrieveUpdateDeleteView
from ApiDrinkSaver.views.priceModification_view import PriceModificationListCreateView, PriceModificationRetrieveUpdateDeleteView

urlpatterns = [
    # Authentification
    path('token/', obtain_auth_token, name='token'),
    # Utilisateurs Lambdas
    path('users/', UserLambdaListView.as_view(), name='user-lambda-list'),
    path('users/<int:pk>/', UserLambdaDetailView.as_view(), name='user-lambda-detail'),
    # Bars
    path('bars/', BarListCreateView.as_view(), name='bar-list-create'),
    path('bars/<int:pk>/', BarRetrieveUpdateDeleteView.as_view(), name='bar-retrieve-update-delete'),
    # Drink Prices
    path('drink-prices/', DrinkPriceListCreateView.as_view(), name='drink-price-list-create'),
    path('drink-prices/<int:pk>/', DrinkPriceRetrieveUpdateDeleteView.as_view(), name='drink-price-retrieve-update'
                                                                                      '-delete'),
]
