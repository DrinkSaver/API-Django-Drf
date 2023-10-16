from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ApiDrinkSaver.views.user_view import (UserRegistrationView, UserLoginView, UserProfileView ,PasswordResetView,
                                           PasswordResetConfirmView)


class UserRegistrationTest(APITestCase):
    @classmethod
    def as_view(cls):
        view = UserRegistrationView.as_view()
        return lambda request, *args, **kwargs: view(request, *args, **kwargs)

    def test_user_registration(self):
        url = reverse('user-registration')
        data = {
            'email': 'test@example.com',
            'password': 'password123',
            # Autres champs requis pour l'inscription
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registration_invalid_data(self):
        url = reverse('user-registration')
        data = {
            'email': 'test@example.com',  # Laissez le champ du mot de passe manquant
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLoginTest(APITestCase):
    @classmethod
    def as_view(cls):
        view = UserLoginView.as_view()
        return lambda request, *args, **kwargs: view(request, *args, **kwargs)

    def test_user_login(self):
        url = reverse('user-login')
        data = {
            'email': 'test@example.com',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_invalid_credentials(self):
        url = reverse('user-login')
        data = {
            'email': 'test@example.com',
            'password': 'wrong-password',  # Mot de passe incorrect
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PasswordResetTest(APITestCase):
    @classmethod
    def as_view(cls):
        view = PasswordResetView.as_view()
        return lambda request, *args, **kwargs: view(request, *args, **kwargs)

    def test_password_reset_request(self):
        url = reverse('password-reset')
        data = {
            'email': 'test@example.com',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_password_reset_request_invalid_email(self):
        url = reverse('password-reset')
        data = {
            'email': 'nonexistent@example.com',  # Adresse e-mail inexistante
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmTest(APITestCase):
    @classmethod
    def as_view(cls):
        view = PasswordResetConfirmView.as_view()
        return lambda request, *args, **kwargs: view(request, *args, **kwargs)

    def test_password_reset_confirm(self):
        url = reverse('password-reset-confirm')
        data = {
            'email': 'test@example.com',
            'confirmation_code': '123456',
            'new_password': 'newpassword123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_password_reset_confirm_invalid_code(self):
        url = reverse('password-reset-confirm')
        data = {
            'email': 'test@example.com',
            'confirmation_code': '999999',  # Code de confirmation incorrect
            'new_password': 'newpassword123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserDetailsTest(APITestCase):
    @classmethod
    def as_view(cls):
        view = UserProfileView.as_view()
        return lambda request, *args, **kwargs: view(request, *args, **kwargs)

    def test_user_details(self):
        url = reverse('user-details')
        # Authentifiez-vous ici en tant qu'utilisateur avec un jeton JWT valide
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
