import unittest
from django.test import TestCase
from django.urls import reverse
from ApiDrinkSaver.models.user import CustomUser


class UserManagementTest(TestCase):

    def setUp(self):
        # Vous pouvez ajouter ici des données d'exemple pour vos tests
        self.user = CustomUser.objects.create_user(
            email="testuser@example.com",
            password="testpassword"
        )

    def test_create_user(self):
        # Testez la création d'un nouvel utilisateur
        user = CustomUser.objects.create_user(
            email="testuser@example.com",
            password="testpassword"
        )
        self.assertIsInstance(user, CustomUser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_user_authentication(self):
        # Testez l'authentification de l'utilisateur
        login_data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, 200)
        # Assurez-vous que l'utilisateur est connecté
        user = CustomUser.objects.get(email=login_data['email'])
        self.assertTrue(user.is_authenticated)

    def test_admin_user(self):
        # Testez la création d'un superutilisateur
        admin = CustomUser.objects.create_superuser(
            email="admin@example.com",
            password="adminpassword"
        )
        self.assertIsInstance(admin, CustomUser)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    # Ajoutez d'autres méthodes de test pour couvrir les fonctionnalités de gestion des utilisateurs


if __name__ == '__main__':
    unittest.main()
