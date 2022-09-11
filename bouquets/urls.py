"""Imports from django and views."""
from django.urls import path
from . import views

# Url link to the bouquet page
urlpatterns = [
    path('', views.all_bouquets, name='bouquets')
]
