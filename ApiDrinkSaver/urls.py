from django.urls import path
from ApiDrinkSaver.views.user_view import (UserRegistrationView, UserLoginView, PasswordResetView,
                                           PasswordResetConfirmView)

from ApiDrinkSaver.tests.user_test import (UserRegistrationTest, UserLoginTest, UserDetailsTest, PasswordResetTest,
                                           PasswordResetConfirmTest)

from ApiDrinkSaver.views.product_view import (ProductList, ProductDetail, BarList, BarDetail, BarProductPriceList,
                                              BarProductPriceDetail)
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('bars/', BarList.as_view(), name='bar-list'),
    path('bars/<int:pk>/', BarDetail.as_view(), name='bar-detail'),
    path('prices/', BarProductPriceList.as_view(), name='price-list'),
    path('prices/<int:pk>/', BarProductPriceDetail.as_view(), name='price-detail'),

    path('test/registration/', UserRegistrationTest.as_view(), name='test-registration'),
    path('test/login/', UserLoginTest.as_view(), name='test-login'),
    path('test/details', UserDetailsTest.as_view(), name='test-details'),
    path('test/password/reset/', PasswordResetTest.as_view(), name='test-password-reset'),
    path('test/password/reset/confirm/', PasswordResetConfirmTest.as_view(), name='test-password-reset-confirm'),
]
