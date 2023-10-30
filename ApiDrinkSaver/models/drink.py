from django.db import models
from django.utils.translation import gettext_lazy as _
from ApiDrinkSaver.models.categoryDrink import CategoryDrink


class Drink(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('name'),
        help_text=_('The name of the drink.')
    )
    category = models.ForeignKey(CategoryDrink, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name=_('category'))

    image = models.ImageField(
        upload_to='drink_images/',
        null=True,
        blank=True,
        verbose_name=_('image'),
        help_text=_('Optional. Upload an image of the drink.')
    )
    ingredients = models.TextField(
        verbose_name=_('ingredients'),
        help_text=_('The list of ingredients in the drink.')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('description'),
        help_text=_('Optional. Description of the drink.')
    )
    alcohol_content = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('alcohol content'),
        help_text=_('Optional. Alcohol content of the drink.')
    )
    volume = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('volume'),
        help_text=_('Optional. Volume of the drink in milliliters.')
    )

    bars = models.ManyToManyField(
        'Bar',
        through='DrinkPrice',
        related_name='drinks',
        verbose_name=_('bars'),
        help_text=_('Select the bars where the drink is available and specify prices.')
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Drink'
        verbose_name = _('drink')
        verbose_name_plural = _('drinks')
