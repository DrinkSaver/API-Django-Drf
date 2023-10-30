from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserLambda(AbstractUser):
    # Champs utilisateur standard
    email = models.EmailField(
        unique=True,
        verbose_name=_('email'),
        help_text=_('Required. Your unique email address for authentication.')
    )

    username = models.CharField(
        unique=True,
        verbose_name=_('username'),
        max_length=150,
        help_text=_('Required. Your unique username for authentication.')
    )

    password = models.CharField(
        max_length=128,
        verbose_name=_('password'),
        help_text=_('Required. Your password for authentication.')
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_('first name'),
        help_text=_('Optional. Your first name.')
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_('last name'),
        help_text=_('Optional. Your last name.')
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('date of birth'),
        help_text=_('Optional. Your date of birth (YYYY-MM-DD).')
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True,
        verbose_name=_('profile picture'),
        help_text=_('Optional. Upload your profile picture.')
    )
    favorite_drinks = models.ManyToManyField(
        'Drink',
        related_name='favorite_by',
        blank=True,
        verbose_name=_('favorite drinks'),
        help_text=_('Add your favorite drinks to the list.')
    )

    drink_price_modifications = models.ManyToManyField(
        'Drink',
        through='PriceModification',
        related_name='price_modifications',
        verbose_name=_('drink price modifications'),
        help_text=_('View your drink price modification history.')
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'UserLambda'
        verbose_name = _('user')
        verbose_name_plural = _('users')


