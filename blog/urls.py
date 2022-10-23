"""Imports from django and views."""
from django.urls import path
from . import views

# Url link to the contact page
urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/post/', views.add_post, name='add_post'),
    path('edit/<int:comment_id>/<slug:slug>/', views.edit_comment, name='edit_comment'),
    path('delete/<int:comment_id>/<slug:slug>/', views.delete_comment, name='delete_comment'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]