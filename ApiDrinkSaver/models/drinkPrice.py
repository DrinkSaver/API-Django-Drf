from django.db import models
from django.utils.translation import gettext_lazy as _
from ApiDrinkSaver.models.drink import Drink
from ApiDrinkSaver.models.bar import Bar


class DrinkPrice(models.Model):
    bar = models.ForeignKey(
        Bar,
        on_delete=models.CASCADE,
        verbose_name=_('bar')
    )

    drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE,
        verbose_name=_('drink')
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_('price')
    )

    def __str__(self):
        return f"{self.bar.name} - {self.drink.name}"

    class Meta:
        db_table = 'DrinkPrice'
        verbose_name = _('drink price')
        verbose_name_plural = _('drink prices')
