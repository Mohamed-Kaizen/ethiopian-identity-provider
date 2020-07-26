"""Collection views."""
from django.utils import timezone
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Renew
from .serializers import (
    BusinessSerializer,
    UserInfoSerializer,
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


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def accepted_business_api(request: Request) -> Response:
    """Accepted business end point."""
    businesses = request.user.businesses.filter(status="Accepted")

    serializer = BusinessSerializer(businesses, many=True)

    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def requested_business_api(request: Request) -> Response:
    """Requested business end point."""
    businesses = request.user.businesses.filter(status="Requested")

    serializer = BusinessSerializer(businesses, many=True)

    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def renew_api(request: Request) -> Response:
    """Renew end point."""
    if request.user.expired_at > timezone.now():
        return Response(
            {"detail": "Your account has not been expired yet"},
            status.HTTP_400_BAD_REQUEST,
        )

    Renew.objects.create(user=request.user)

    return Response(
        {"detail": "You send renew request successfully"}, status.HTTP_201_CREATED
    )
