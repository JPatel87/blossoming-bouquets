"""Imports from django and views."""
from django.urls import path
from . import views

# Url link to the contact page
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]