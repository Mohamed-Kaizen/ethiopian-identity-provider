"""Users URL Configuration."""
from django.urls import include, path

from .views import (
    BusinessCreateAPI,
    OauthAcceptedBusinessAPI,
    OauthRequestedBusinessAPI,
    OauthUserInfoAPI,
    OauthUserProfileAPI,
    UsersListAPI,
    accepted_business_api,
    renew_api,
    requested_business_api,
)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("business/", BusinessCreateAPI.as_view()),
    path("business/accepted/", accepted_business_api),
    path("business/requested/", requested_business_api),
    path("renew/", renew_api),
    path("o/userinfo/", OauthUserInfoAPI.as_view()),
    path("o/profile/", OauthUserProfileAPI.as_view()),
    path("o/business/accepted/", OauthAcceptedBusinessAPI.as_view()),
    path("o/business/requested/", OauthRequestedBusinessAPI.as_view()),
    path("", UsersListAPI.as_view()),
]
