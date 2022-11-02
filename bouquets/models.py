""" Imports from django. """
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """
    Category model for database.
    """
    class Meta:
        """ Display category model name as categories in admin view. """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        """ Display category instance by its name. """
        return str(self.name)


class Bouquet(models.Model):
    """
    Bouquet model for database.
    """
    category = models.ForeignKey(
        'Category', null=True,
        blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('15.00')),
                    MaxValueValidator(Decimal('100.00'))])
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ Display bouquet instance by its name. """
        return str(self.name)
