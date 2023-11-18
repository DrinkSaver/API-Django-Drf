from django.db import models
from django.utils.translation import gettext_lazy as _


class BarFilter(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('name'),
        help_text=_('Name of the filter')
    )

    description = models.TextField(
        blank=True,
        verbose_name=_('description'),
        help_text=_('Description of the filter')
    )

    smoking = models.BooleanField(
        default=False,
        verbose_name=_('smoking'),
        help_text=_('Does the bar allow smoking?')
    )

    wifi = models.BooleanField(
        default=False,
        verbose_name=_('WiFi'),
        help_text=_('Does the bar have WiFi?')
    )

    terrace = models.BooleanField(
        default=False,
        verbose_name=_('has terrace'),
        help_text=_('Does the bar have a terrace?')
    )

    payment_methods = models.CharField(
        max_length=100,
        verbose_name=_('payment methods'),
        help_text=_('Accepted payment methods')
    )

    minimum_card_payment = models.DecimalField(
        max_digits=6, decimal_places=2,
        verbose_name=_('minimum card payment'),
        help_text=_('Minimum payment amount for card transactions')
    )
    has_karaoke = models.BooleanField(
        default=False,
        verbose_name=_('has karaoke'),
        help_text=_('Does the bar have karaoke?')
    )

    has_happy_hour = models.BooleanField(
        default=False,
        verbose_name=_('has happy hour'),
        help_text=_('Does the bar have a happy hour?')
    )
    is_accessible_for_disabled = models.BooleanField(
        default=False,
        verbose_name=_('accessible for disabled'),
        help_text=_('Is the bar accessible for disabled individuals?')
    )

    opening_hours = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_('opening hours'),
        help_text=_('Bar opening hours')
    )

    has_sports_broadcast = models.BooleanField(
        default=False,
        verbose_name=_('sports broadcast'),
        help_text=_('Does the bar broadcast sports events?')
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'BarFilter'
        verbose_name = _('bar filter')
        verbose_name_plural = _('bar filters')
