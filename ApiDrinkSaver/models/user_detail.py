# user_models.py
from django.db import models
from django.contrib.auth.models import User  # Utilisez votre modèle CustomUser si vous l'avez personnalisé

from ApiDrinkSaver.models.product_bar import Product, Bar


class UserFavoriteBar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)


class UserFavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class UserModifiedBarPrice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
