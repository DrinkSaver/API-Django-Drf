from django.urls import path
from ApiDrinkSaver.views.user_view import (UserRegistrationView, UserLoginView, PasswordResetView,
                                           PasswordResetConfirmView)

from ApiDrinkSaver.tests.user_test import (UserRegistrationTest, UserLoginTest, UserDetailsTest, PasswordResetTest,
                                           PasswordResetConfirmTest)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    path('test/registration/', UserRegistrationTest.as_view(), name='test-registration'),
    path('test/login/', UserLoginTest.as_view(), name='test-login'),
    path('test/details', UserDetailsTest.as_view(), name='test-details'),
    path('test/password/reset/', PasswordResetTest.as_view(), name='test-password-reset'),
    path('test/password/reset/confirm/', PasswordResetConfirmTest.as_view(), name='test-password-reset-confirm'),
]
