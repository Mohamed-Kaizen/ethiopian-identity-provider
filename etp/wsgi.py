"""WSGI config for Ethiopian Identity Provider project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "etp.settings")

application = get_wsgi_application()
