from django import forms
from django.core import validators
from .models import Contact


class ContactForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Name'}),
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder':'Email'}),
        validators=[validators.EmailValidator(message="Invalid Email")]
    )

    query = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Please enter your query details'}),
    )

    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'subject': forms.RadioSelect()
        }