from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your enquiry, we will get back to soon!')

            return redirect('contact')
        else:
            messages.error(request, 'Failed to send enquiry. Please ensure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
