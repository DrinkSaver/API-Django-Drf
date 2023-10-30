from django.db import models
from django.utils.translation import gettext_lazy as _
from ApiDrinkSaver.models.bar import Bar


class AlcoholGame(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('name'),
        help_text=_('Name of the alcohol game')
    )

    description = models.TextField(
        blank=True,
        verbose_name=_('description'),
        help_text=_('Description of the alcohol game')
    )

    bars = models.ManyToManyField(
        Bar,
        verbose_name=_('bars'),
        help_text=_('Bars where the game is available')
    )

    rules = models.TextField(
        blank=True,
        verbose_name=_('rules'),
        help_text=_('Rules and instructions for playing the game')
    )

    image = models.ImageField(
        upload_to='alcohol_game_images/',
        null=True,
        blank=True,
        verbose_name=_('image'),
        help_text=_('Image for the alcohol game')
    )

    start_date = models.DateField(
        verbose_name=_('start date'),
        help_text=_('Start date of the game')
    )

    end_date = models.DateField(
        verbose_name=_('end date'),
        help_text=_('End date of the game')
    )

    equipment = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_('equipment'),
        help_text=_('Equipment required for the game')
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'AlcoholGame'
        verbose_name = _('alcohol game')
        verbose_name_plural = _('alcohol games')
