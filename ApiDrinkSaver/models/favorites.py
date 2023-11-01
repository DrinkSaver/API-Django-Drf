# favorites/models.py

from django.db import models
from django.contrib.auth import get_user_model
from ApiDrinkSaver.models.drink import Drink
from ApiDrinkSaver.models.bar import Bar

UserLambda = get_user_model()


class FavoriteDrink(models.Model):
    user = models.ForeignKey(
        UserLambda,
        on_delete=models.CASCADE
    )

    drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE
    )

    date_added = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'drink')

    def __str__(self):
        return f"{self.user.username}'s Favorite Drink"


class FavoriteBar(models.Model):
    user = models.ForeignKey(
        UserLambda,
        on_delete=models.CASCADE
    )

    bar = models.ForeignKey(
        Bar,
        on_delete=models.CASCADE
    )

    date_added = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'bar')

    def __str__(self):
        return f"{self.user.username}'s Favorite Bar"
