"""Imports from django and views."""
from django.urls import path
from . import views

# Url link to blog pages
urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete_post'),
    path('edit_comment/<int:comment_id>/<slug:slug>/', views.edit_comment, name='edit_comment'),
    path(
        'delete_comment/<int:comment_id>/<slug:slug>/',
        views.delete_comment, name='delete_comment'
        ),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
