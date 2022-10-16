from django.db import models


# Create your models here.
class Contact(models.Model):

    SUBJECT_CHOICES = (
        ("Bouquets", "Bouquets"),
        ("Order", "Order"),
        ("Delivery", "Delivery"),
        ("Account", "Account"),
        ("Other", "Other"),
    )

    class Meta:
        """
        Method to display category model name as categories in admin view.
        """
        verbose_name_plural = 'Enquiries'

    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        default="Bouquets"
    )
    query = models.TextField()

    def __str__(self):
        return f"Query about {self.subject} by {self.name}"
