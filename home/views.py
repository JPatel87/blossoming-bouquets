""" Imports from django. """
from django.shortcuts import render


def index(request):
    """ View the home page."""

    return render(request, 'home/index.html')
