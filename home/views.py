"""Imports from django."""
from django.shortcuts import render


def index(request):
    """Function to view the home page."""

    return render(request, 'home/index.html')
