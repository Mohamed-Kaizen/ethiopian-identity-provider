"""View for the etp project."""
from typing import Union

from django.conf import settings
from django.contrib.auth import logout
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect


def home(
    request: WSGIRequest,
) -> Union[HttpResponsePermanentRedirect, HttpResponseRedirect]:
    """View that will redirect to the home page."""
    return redirect(settings.HOME_PAGE_URL)


def sign_out(
    request: WSGIRequest,
) -> Union[HttpResponsePermanentRedirect, HttpResponseRedirect]:
    """View that will redirect to the home page."""
    logout(request)
    return redirect(settings.HOME_PAGE_URL)
