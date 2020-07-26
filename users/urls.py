"""Users URL Configuration."""
from django.urls import include, path

from .views import (
    AcceptedBusinessAPI,
    RequestedBusinessAPI,
    UserInfoAPI,
    UserProfileAPI,
)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("o/userinfo/", UserInfoAPI.as_view()),
    path("o/profile/", UserProfileAPI.as_view()),
    path("o/business/accepted/", AcceptedBusinessAPI.as_view()),
    path("o/business/requested/", RequestedBusinessAPI.as_view()),
]
