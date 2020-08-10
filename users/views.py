"""Collection views."""
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import generics, permissions, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response

from .filter import UserFilter
from .models import Business, CustomUser, Renew
from .serializers import (
    BusinessCreateSerializer,
    BusinessSerializer,
    UserInfoSerializer,
    UserListSerializer,
    UserProfileSerializer,
)


class OauthUserInfoAPI(generics.GenericAPIView):
    """Oauth user info API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    serializer_class = UserInfoSerializer
    required_scopes = ["user"]

    def get(self: "OauthUserInfoAPI", request: Request) -> Response:
        """User info end point."""
        serializer = self.get_serializer(request.user)

        return Response(serializer.data)


class OauthUserProfileAPI(generics.GenericAPIView):
    """Oauth user profile API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    serializer_class = UserProfileSerializer
    required_scopes = ["user:profile"]

    def get(self: "OauthUserProfileAPI", request: Request) -> Response:
        """User profile end point."""
        serializer = self.get_serializer(request.user)

        return Response(serializer.data)


class OauthAcceptedBusinessAPI(generics.GenericAPIView):
    """Oauth accepted business API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    serializer_class = BusinessSerializer
    required_scopes = ["business:accepted"]

    def get(self: "OauthAcceptedBusinessAPI", request: Request) -> Response:
        """Accepted business end point."""
        businesses = request.user.businesses.filter(status="Accepted")

        serializer = self.get_serializer(businesses, many=True)

        return Response(serializer.data)


class OauthRequestedBusinessAPI(generics.GenericAPIView):
    """Oauth requested business API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    serializer_class = BusinessSerializer
    required_scopes = ["business:requested"]

    def get(self: "OauthRequestedBusinessAPI", request: Request) -> Response:
        """Requested business end point."""
        businesses = request.user.businesses.filter(status="Requested")

        serializer = self.get_serializer(businesses, many=True)

        return Response(serializer.data)


class OauthRenewAPI(generics.GenericAPIView):
    """Oauth renew API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ["renew:write"]

    def post(self: "OauthRenewAPI", request: Request) -> Response:
        """Renew create end point."""
        if request.user.expired_at > timezone.now():
            return Response(
                {"detail": _("Your account has not been expired yet")},
                status.HTTP_400_BAD_REQUEST,
            )

        if Renew.objects.filter(user=request.user, status="Requested").first():
            return Response(
                {
                    "detail": _(
                        "You have already send renew request. "
                        "Please wait till it been accepted."
                    )
                },
                status.HTTP_400_BAD_REQUEST,
            )

        Renew.objects.create(user=request.user)

        return Response(
            {"detail": _("You send renew request successfully")},
            status.HTTP_201_CREATED,
        )


class OauthBusinessCreateAPI(generics.GenericAPIView):
    """Oauth business create API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ["business:write"]

    serializer_class = BusinessCreateSerializer

    def post(self: "OauthBusinessCreateAPI", request: Request) -> Response:
        """Business post API."""
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            data = serializer.data

            business_type = data.get("type")

            owners = data.get("owners")

            name = data.get("name")

            if Business.objects.filter(name=name, status="Accepted").first():
                return Response(
                    {"detail": _(f"The name: {name} has been took. Try another name")},
                    status.HTTP_400_BAD_REQUEST,
                )

            new_business = Business.objects.create(
                name=name,
                description=data.get("description"),
                city=data.get("city"),
                sub_city=data.get("sub_city"),
                type=business_type,
                requested_by=request.user,
            )

            new_business.owners.add(request.user)

            if "Sole Proprietorship" != business_type and owners:

                for owner in owners:

                    user = CustomUser.objects.filter(username=owner).first()

                    if user:
                        new_business.owners.add(user)

            return Response(data)


class UsersListAPI(generics.ListAPIView):
    """User list API."""

    queryset = CustomUser.objects.all()

    serializer_class = UserListSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filterset_class = UserFilter

    search_fields = ("pin", "full_name", "username", "email")

    ordering = ("username",)

    ordering_fields = ("full_name", "username", "email")
