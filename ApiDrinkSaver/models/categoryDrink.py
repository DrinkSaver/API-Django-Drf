from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryDrink(models.Model):
    name = models.CharField(
        max_length=50,
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
