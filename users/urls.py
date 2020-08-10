"""Users URL Configuration."""
from django.urls import include, path

from .views import (
    OauthAcceptedBusinessAPI,
    OauthBusinessCreateAPI,
    OauthRenewAPI,
    OauthRequestedBusinessAPI,
    OauthUserInfoAPI,
    OauthUserProfileAPI,
    UsersListAPI,
)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("o/userinfo/", OauthUserInfoAPI.as_view()),
    path("o/profile/", OauthUserProfileAPI.as_view()),
    path("o/renew/", OauthRenewAPI.as_view()),
    path("o/business/accepted/", OauthAcceptedBusinessAPI.as_view()),
    path("o/business/requested/", OauthRequestedBusinessAPI.as_view()),
    path("o/business/", OauthBusinessCreateAPI.as_view()),
    path("", UsersListAPI.as_view()),
]
