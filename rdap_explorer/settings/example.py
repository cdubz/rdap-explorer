"""
Django local settings for rdap_explorer project.
"""

from rdap_explorer.settings.base import *


SECRET_KEY = 'SECRET_KEY'

DEBUG = True

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'page_cache',
    }
}
