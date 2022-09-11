"""Imports from django"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Url links to project apps; home, bouquets,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('bouquets/', include('bouquets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
