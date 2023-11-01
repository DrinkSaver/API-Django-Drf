from django.db import models
from django.contrib.auth import get_user_model
from ApiDrinkSaver.models.drink import Drink
from ApiDrinkSaver.models.bar import Bar

UserLambda = get_user_model()


class FavoriteItem(models.Model):
    ITEM_TYPES = (
        ('drink', 'Drink'),
        ('bar', 'Bar'),
    )

    user = models.ForeignKey(
        UserLambda,
        on_delete=models.CASCADE
    )

    item_type = models.CharField(
        choices=ITEM_TYPES,
        max_length=5
    )

    item_id = models.PositiveIntegerField(
    )

    type = models.CharField(
        max_length=10,
        choices=(
            ('drink', 'Drink'),
            ('bar', 'Bar')
        )
    )

    class Meta:
        unique_together = ('user', 'item_type', 'item_id')

    def __str__(self):
        return f"{self.user.username}'s Favorite {self.item_type.capitalize()}"

