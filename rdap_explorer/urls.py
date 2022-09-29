"""RDAP Explorer URL Configuration
"""
from django.urls import include, path

urlpatterns = [
    path("", include("query.urls")),
]
