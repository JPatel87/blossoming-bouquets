"""Imports from django and views."""
from django.urls import path
from . import views

# Url link to the home page
urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]
