"""Imports from django and views."""
from django.urls import path
from . import views

# Url link to the home page
urlpatterns = [
    path('', views.view_bag, name='view_bag')
]
