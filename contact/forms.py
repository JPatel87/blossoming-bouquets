from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Name'}),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'Email'}),
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