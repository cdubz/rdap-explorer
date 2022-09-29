"""
Paths for the rdap_explorer project, query app.
"""

from django.urls import re_path
from . import views

app_name = 'query'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<query>.*)/results/$', views.results, name='results'),
]
