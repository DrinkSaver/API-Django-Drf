import unittest
from django.test import TestCase
from django.urls import reverse
from ApiDrinkSaver.models.user import CustomUser
from ApiDrinkSaver.models.bar import Bar


class UserManagementTest(TestCase):
    def setUp(self):
        # Crée un utilisateur lambda pour les tests
        self.lambda_user = CustomUser.objects.create_user(
            email="lambda@example.com",
            password="lambdapassword",
            is_lambda_user=True,
        )

        # Crée un propriétaire de bar pour les tests
        self.bar_owner = CustomUser.objects.create_user(
            email="owner@example.com",
            password="ownerpassword",
            is_bar_owner=True,
        )

        # Crée un administrateur pour les tests
        self.admin = CustomUser.objects.create_superuser(
            email="admin@example.com",
            password="adminpassword",
        )

        # Crée un bar pour les tests
        self.bar = Bar.objects.create(
            name="Le Bar Test",
            owner=self.bar_owner,
            address="123 Rue de Test",
        )

    def test_create_user(self):
        # Teste la création d'un utilisateur lambda
        user = CustomUser.objects.create_user(
            email="testuser@example.com",
            password="testpassword",
            is_lambda_user=True,
        )
        self.assertIsInstance(user, CustomUser)
        self.assertTrue(user.is_lambda_user)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_user_authentication(self):
        # Teste l'authentification de l'utilisateur lambda
        login_data = {
            'email': 'lambda@example.com',
            'password': 'lambdapassword',
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, 200)
        # Vérifie que l'utilisateur lambda est connecté
        user = CustomUser.objects.get(email=login_data['email'])
        self.assertTrue(user.is_authenticated)

    def test_admin_user(self):
        # Teste la création d'un super administrateur
        admin = CustomUser.objects.create_superuser(
            email="superadmin@example.com",
            password="superadminpassword",
        )
        self.assertIsInstance(admin, CustomUser)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_update_user_profile(self):
        # Teste la mise à jour du profil utilisateur
        user = self.lambda_user
        self.client.force_login(user)
        updated_data = {
            'first_name': 'UpdatedFirstName',
            'last_name': 'UpdatedLastName',
        }
        response = self.client.put(reverse('update-user-profile'), updated_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        user.refresh_from_db()
        self.assertEqual(user.first_name, updated_data['first_name'])
        self.assertEqual(user.last_name, updated_data['last_name'])

    def test_search_users(self):
        # Teste la recherche d'utilisateurs par nom, prénom ou adresse e-mail
        user = self.lambda_user
        self.client.force_login(user)
        query = 'owner'
        response = self.client.get(reverse('search-users'), {'q': query})
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['email'], self.bar_owner.email)

    def test_get_user_by_id(self):
        # Teste la récupération du profil utilisateur par son ID
        user = self.lambda_user
        self.client.force_login(user)
        response = self.client.get(reverse('get-user-by-id', args=[self.bar_owner.id]))
        self.assertEqual(response.status_code, 200)
        user_data = response.json()
        self.assertEqual(user_data['email'], self.bar_owner.email)

    def test_admin_access_to_views(self):
        # Teste l'accès aux vues réservées aux administrateurs
        admin = self.admin
        self.client.force_login(admin)

        # Teste l'accès à la liste de tous les utilisateurs
        response = self.client.get(reverse('get-all-users'))
        self.assertEqual(response.status_code, 200)

        # Teste l'accès à la liste paginée des utilisateurs
        response = self.client.get(reverse('get-paginated-users'))
        self.assertEqual(response.status_code, 200)

    def test_lambda_cannot_modify_price(self):
        # Teste qu'un utilisateur lambda ne peut pas modifier le prix d'une boisson
        user = self.lambda_user
        self.client.force_login(user)
        response = self.client.put(
            reverse('update-bar-product-price', args=[self.bar.id, self.bar.products.first().id]), {})
        self.assertEqual(response.status_code, 403)

    # Ajoutez d'autres méthodes de test pour couvrir les fonctionnalités de gestion des utilisateurs


if __name__ == '__main__':
    unittest.main()
