"""
Paths for the rdap_explorer project, query app.
"""

from django.conf.urls import url
from . import views

app_name = 'query'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<query>.*)/results/$', views.results, name='results'),
]
