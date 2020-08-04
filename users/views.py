"""Collection views."""
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
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


class UsersListAPI(generics.ListAPIView):
    """User list API."""

    queryset = CustomUser.objects.all()

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserListSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filterset_class = UserFilter

    search_fields = ("pin", "full_name", "username", "email")

    ordering = ("username",)

    ordering_fields = ("full_name", "username", "email")


class BusinessCreateAPI(generics.GenericAPIView):
    """Business create API."""

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = BusinessCreateSerializer

    def post(self: "BusinessCreateAPI", request: Request) -> Response:
        """Business post API."""
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            data = serializer.data

            business_type = data.get("type")

            owners = data.get("owners")

            new_business = Business.objects.create(
                name=data.get("name"),
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
