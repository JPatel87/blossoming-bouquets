""" Imports from django and views. """
from django.urls import path
from . import views

# Url link to profile pages
urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
