""" Imports from django model. """
from django.db import models


class Contact(models.Model):
    """ Contact model for database. """

    SUBJECT_CHOICES = (
        ("Bouquets", "Bouquets"),
        ("Order", "Order"),
        ("Delivery", "Delivery"),
        ("Account", "Account"),
        ("Other", "Other"),
    )

    class Meta:
        """ Display category model name as categories. """
        verbose_name_plural = 'Enquiries'
        ordering = ['-date']

    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        default="Bouquets"
    )
    query = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Display contact instance by subject and person name. """
        return f"Query about {self.subject} by {self.name}"
