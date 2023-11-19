from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from ApiDrinkSaver.models.userLambda import UserLambda
from ApiDrinkSaver.models.bar import Bar
from ApiDrinkSaver.models.drink import Drink

MODIFICATION_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('APPROVED', 'Approved'),
    ('REJECTED', 'Rejected'),
)


class PriceModification(models.Model):
    user = models.ForeignKey(
        UserLambda,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )

    drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE,
        verbose_name=_('drink')
    )

    bar = models.ForeignKey(
        Bar,
        on_delete=models.CASCADE,
        verbose_name=_('bar')
    )

    new_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name=_('new price')
    )

    status = models.CharField(
        max_length=20,
        choices=MODIFICATION_STATUS_CHOICES,
        default='PENDING',
        verbose_name=_('status'),
        help_text=_('Status of the price modification request.')
    )

    date_modified = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('date modified')
    )

    is_pending = models.BooleanField(
        default=True,
        verbose_name=_('is pending')
    )

    is_approved = models.BooleanField(
        default=False,
        verbose_name=_('is approved')
    )

    def __str__(self):
        return f"{self.user.username} - {self.drink.name} - ${self.new_price}"

    class Meta:
        db_table = 'PriceModification'
        verbose_name = _('price modification')
        verbose_name_plural = _('price modifications')
