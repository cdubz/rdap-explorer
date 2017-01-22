"""rdap_explorer URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('query.urls')),
]
