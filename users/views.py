"""Collection views."""
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import generics, permissions
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import (
    BusinessSerializer,
    UserInfoSerializer,
    UserProfileSerializer,
)


class UserInfoAPI(generics.GenericAPIView):
    """Oauth user info API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    serializer_class = UserInfoSerializer
    required_scopes = ["user"]

    def get(self: "UserInfoAPI", request: Request) -> Response:
        """User info end point."""
        serializer = self.get_serializer(request.user)

        return Response(serializer.data)


class UserProfileAPI(generics.GenericAPIView):
    """Oauth user profile API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    serializer_class = UserProfileSerializer
    required_scopes = ["user:profile"]

    def get(self: "UserProfileAPI", request: Request) -> Response:
        """User profile end point."""
        serializer = self.get_serializer(request.user)

        return Response(serializer.data)


class AcceptedBusinessAPI(generics.GenericAPIView):
    """Oauth accepted business API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    serializer_class = BusinessSerializer
    required_scopes = ["business:accepted"]

    def get(self: "AcceptedBusinessAPI", request: Request) -> Response:
        """Accepted business end point."""
        businesses = request.user.businesses.filter(status="Accepted")

        serializer = self.get_serializer(businesses, many=True)

        return Response(serializer.data)


class RequestedBusinessAPI(generics.GenericAPIView):
    """Oauth requested business API."""

    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    serializer_class = BusinessSerializer
    required_scopes = ["business:requested"]

    def get(self: "RequestedBusinessAPI", request: Request) -> Response:
        """Requested business end point."""
        businesses = request.user.businesses.filter(status="Requested")

        serializer = self.get_serializer(businesses, many=True)

        return Response(serializer.data)
