"""Imports from django and contact form."""
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    Function to view contact us form.

    If the form is valid,
    a success message is displayed
    and the contact page is returned.
    If invalid, error message is displayed.
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for your enquiry,\
                we will get back to soon!')

            return redirect('contact')
        else:
            messages.error(
                request,
                'Failed to send enquiry.\
                Check form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
