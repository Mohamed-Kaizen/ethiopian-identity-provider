"""ASGI config for Ethiopian Identity Provider project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "etp.settings")

application = get_asgi_application()
