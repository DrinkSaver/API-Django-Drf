from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from ApiDrinkSaver.models.user import CustomUser


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_user_profile(self):
        # Test de récupération du profil de l'utilisateur
        response = self.client.get('/user/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_profile(self):
        # Test de mise à jour du profil de l'utilisateur
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'bio': 'New bio'
        }
        response = self.client.put('/user/profile/update/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'John')

    def test_password_reset(self):
        # Test de la réinitialisation du mot de passe
        data = {
            'email': 'testuser@example.com'
        }
        response = self.client.post('/password/reset/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_email_registration(self):
        # Test de l'inscription par email
        data = {
            'email': 'newuser@example.com',
            'password': 'newpassword'
        }
        response = self.client.post('/registration/email/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_google_registration(self):
        # Test de l'inscription via Google
        # Assurez-vous d'utiliser des clés et des données d'accès factices ici
        data = {
            'access_token': 'your_google_access_token'
        }
        response = self.client.post('/registration/google/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_facebook_registration(self):
        # Test de l'inscription via Facebook
        # Assurez-vous d'utiliser des clés et des données d'accès factices ici
        data = {
            'access_token': 'your_facebook_access_token'
        }
        response = self.client.post('/registration/facebook/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login(self):
        # Test de la connexion
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post('/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
