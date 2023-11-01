from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from ApiDrinkSaver.models.userLambda import UserLambda
from ApiDrinkSaver.models.drink import Drink
from ApiDrinkSaver.models.barFilter import BarFilter


class Bar(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='bar_owner',
        verbose_name=_('owner')
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('name'),
        help_text=_('The name of the bar.')
    )

    email = models.EmailField(
        verbose_name=_('e-mail'),
        help_text=_('E-mail address for registration.')
    )

    password = models.CharField(
        max_length=100,
        verbose_name=_('password'),
        help_text=_('Password for registration.')
    )

    description = models.TextField(
        blank=True,
        verbose_name=_('description'),
        help_text=_('Optional. Description of the bar.')
    )

    location = models.CharField(
        max_length=100,
        verbose_name=_('location'),
        help_text=_('The location of the bar.')
    )

    image = models.ImageField(
        upload_to='bar_images/',
        null=True,
        blank=True,
        verbose_name=_('image'),
        help_text=_('Optional. Upload an image representing the bar.')
    )

    carousel_images = models.ImageField(
        upload_to='carousel_images/',
        null=True,
        blank=True,
        verbose_name=_('carousel images'),
        help_text=_('Upload images for the carousel.')
    )

    menu = models.ManyToManyField(
        Drink,
        through='DrinkPrice',
        verbose_name=_('drinks'),
        help_text=_('Available drinks in the bar')
    )

    filters = models.ManyToManyField(
        BarFilter,
        blank=True,
        verbose_name=_('filters'),
        help_text=_('Filters for the bar')
    )

    favorite_by = models.ManyToManyField(
        UserLambda,
        related_name="favorite_bars",
        blank=True,
        verbose_name=_('favorite_by'),
        help_text=_('Favoris for the bar')
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Bar'
        verbose_name = _('bar')
        verbose_name_plural = _('bars')
