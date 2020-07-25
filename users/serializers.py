"""Collection serializers."""
from django_countries.serializer_fields import CountryField
from rest_framework import serializers


class UserDetailsSerializer(serializers.Serializer):
    """User detail serializer."""

    email = serializers.EmailField(read_only=True)

    username = serializers.CharField(read_only=True)

    picture = serializers.ImageField(read_only=True)

    is_active = serializers.BooleanField(read_only=True)


class JWTSerializer(serializers.Serializer):
    """JWT serializer."""

    access_token = serializers.CharField(read_only=True)

    refresh_token = serializers.CharField(read_only=True)

    user = UserDetailsSerializer(read_only=True)


class ProfileSerializer(serializers.Serializer):
    """Profile serializer."""

    username = serializers.CharField(read_only=True)

    email = serializers.EmailField(read_only=True)

    personal_identity_number = serializers.CharField(read_only=True, source="pin")

    full_name = serializers.CharField(read_only=True)

    picture = serializers.ImageField(read_only=True)

    phone_number = serializers.CharField(read_only=True)

    born = CountryField(read_only=True, country_dict=True)

    nationality = CountryField(read_only=True, country_dict=True)

    date_of_birth = serializers.DateTimeField(read_only=True)

    date_joined = serializers.DateTimeField(read_only=True)

    expired_at = serializers.DateTimeField(read_only=True)
