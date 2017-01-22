"""
WSGI config for rdap_explorer project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rdap_explorer.settings")

application = get_wsgi_application()
