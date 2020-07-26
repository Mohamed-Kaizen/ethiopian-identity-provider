"""View for the etp project."""
from typing import Union

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect


def home(
    request: WSGIRequest,
) -> Union[HttpResponsePermanentRedirect, HttpResponseRedirect]:
    """View that will redirect to the home page."""
    return redirect(settings.HOME_PAGE_URL)
