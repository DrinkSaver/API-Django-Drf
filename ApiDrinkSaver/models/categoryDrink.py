# models/categoryDrink.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryDrink(models.Model):
    class CategoryType(models.TextChoices):
        APERITIFS = 'Apéritifs', _('Apéritifs')
        BIERES = 'Bières', _('Bières')
        COCKTAILS = 'Cocktails', _('Cocktails')
        LIQUEURS = 'Liqueurs', _('Liqueurs')
        SHOTS = 'Shots', _('Shots')
        SPIRITUEUX = 'Spiritueux', _('Spiritueux')
        SOFTS = 'Softs', _('Softs')
        VINS = 'Vins', _('Vins')

    name = models.CharField(
        max_length=50,
        choices=CategoryType.choices,
        unique=True,
        verbose_name=_('name'),
        help_text=_('The name of the drink category, e.g., wine, beer, soft, etc.')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('description'),
        help_text=_('Optional. Description of the drink category.')
    )
    image = models.ImageField(
        upload_to='category_images/',
        null=True,
        blank=True,
        verbose_name=_('image'),
        help_text=_('Optional. Upload an image representing the category.')
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CategoryDrink'
        verbose_name = _('drink category')
        verbose_name_plural = _('drink categories')


# Ajout des catégories
CategoryDrink.objects.create(name="Apéritifs")
CategoryDrink.objects.create(name="Bières")
CategoryDrink.objects.create(name="Cocktails")
CategoryDrink.objects.create(name="Liqueurs")
CategoryDrink.objects.create(name="Shots")
CategoryDrink.objects.create(name="Spiritueux")
CategoryDrink.objects.create(name="Softs")
CategoryDrink.objects.create(name="Vins")
