from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your email, we will get back to soon!')
        else:
            messages.error(request, 'Your email failed to send. Please re-check information.')

    form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
