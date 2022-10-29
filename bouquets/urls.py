"""Imports from django and views."""
from django.urls import path
from . import views

# Url links to bouquet pages
urlpatterns = [
    path('', views.all_bouquets, name='bouquets'),
    path('<int:bouquet_id>/', views.bouquet_detail, name='bouquet_detail'),
    path('add/', views.add_bouquet, name='add_bouquet'),
    path('edit/<int:bouquet_id>/', views.edit_bouquet, name='edit_bouquet'),
    path('delete/<int:bouquet_id>/',
         views.delete_bouquet,
         name='delete_bouquet'
         ),
]
