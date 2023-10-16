from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Bar(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    opening_hours = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BarProductPrice(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class BarTag(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)


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


class AlcoholGeneralDangers(models.Model):
    danger_description = models.TextField()


class GeneralEvents(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_date = models.DateField()
    event_location = models.CharField(max_length=255)


class AlcoholGames(models.Model):
    game_name = models.CharField(max_length=255)
    game_description = models.TextField()
