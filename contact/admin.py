from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    """
    Contact model view on django admin for admin user.
    """

    list_display = (
        'name',
        'email',
        'subject',
        'date',
    )

admin.site.register(Contact, ContactAdmin)
