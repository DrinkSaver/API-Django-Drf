from django.db import models
from django.utils.translation import gettext_lazy as _
from ApiDrinkSaver.models.bar import Bar


class Event(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('name'),
        help_text=_('Name of the event')
    )

    description = models.TextField(
        blank=True,
        verbose_name=_('description'),
        help_text=_('Description of the event')
    )

    bars = models.ManyToManyField(
        Bar,
        verbose_name=_('bars'),
        help_text=_('Bars where the event is taking place')
    )

    date = models.DateTimeField(
        verbose_name=_('date'),
        help_text=_('Date and time of the event')
    )

    location = models.CharField(
        max_length=100,
        verbose_name=_('location'),
        help_text=_('Location of the event')
    )

    image = models.ImageField(
        upload_to='event_images/',
        null=True,
        blank=True,
        verbose_name=_('image'),
        help_text=_('Image for the event')
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Event'
        verbose_name = _('event')
        verbose_name_plural = _('events')
