""" Imports from django, widgets and bouquet model. """
from django import forms
from .widgets import CustomClearableFileInput
from .models import Bouquet


class BouquetForm(forms.ModelForm):
    """
    Bouquet form to add or edit for admin only.
    """

    class Meta:
        """
        Define bouquet form fields and widgets.
        """
        model = Bouquet
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False, widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-0'
