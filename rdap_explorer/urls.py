"""rdap_explorer URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('query.urls')),
    url(r'^query/', include('query.urls')),
    url(r'^admin/', admin.site.urls),
]
