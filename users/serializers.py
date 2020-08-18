"""Collection serializers."""
from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from .models import BusinessType


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

    has_expired = serializers.BooleanField(read_only=True)

    expired_natural_time = serializers.CharField(read_only=True, source="natural_time")

    expired_natural_day = serializers.CharField(read_only=True, source="natural_day")


class UserInfoSerializer(serializers.Serializer):
    """User info serializer."""

    uuid = serializers.UUIDField(read_only=True)

    username = serializers.CharField(read_only=True)

    email = serializers.EmailField(read_only=True)

    picture = serializers.ImageField(read_only=True)

    has_expired = serializers.BooleanField(read_only=True)

    expired_natural_time = serializers.CharField(read_only=True, source="natural_time")

    expired_natural_day = serializers.CharField(read_only=True, source="natural_day")


class AddressSerializer(serializers.Serializer):
    """Address serializer."""

    country = CountryField(read_only=True, country_dict=True)

    city = serializers.CharField(read_only=True)

    street = serializers.CharField(read_only=True)

    house_number = serializers.CharField(read_only=True)


class FingerprintSerializer(serializers.Serializer):
    """Fingerprint serializer."""

    picture = serializers.ImageField(read_only=True)


class UserProfileSerializer(serializers.Serializer):
    """User profile serializer."""

    personal_identity_number = serializers.CharField(read_only=True, source="pin")

    full_name = serializers.CharField(read_only=True)

    phone_number = serializers.CharField(read_only=True)

    date_of_birth = serializers.DateTimeField(read_only=True)

    born = CountryField(read_only=True, country_dict=True)

    nationality = CountryField(read_only=True, country_dict=True)

    expired_at = serializers.DateTimeField(read_only=True)

    addresses = AddressSerializer(read_only=True, many=True)

    fingerprints = FingerprintSerializer(read_only=True, many=True)


class BusinessSerializer(serializers.Serializer):
    """Business serializer."""

    name = serializers.CharField(read_only=True)

    description = serializers.CharField(read_only=True)

    city = serializers.CharField(read_only=True)

    sub_city = serializers.CharField(read_only=True)

    type = serializers.ChoiceField(choices=BusinessType.choices)

    owners = serializers.StringRelatedField(many=True, required=False)

    is_active = serializers.BooleanField(read_only=True)

    create_at = serializers.DateTimeField(read_only=True)

    natural_time = serializers.CharField(read_only=True)

    natural_day = serializers.CharField(read_only=True)


class UserListSerializer(serializers.Serializer):
    """User list serializer."""

    id = serializers.UUIDField(read_only=True, source="pin")

    username = serializers.CharField(read_only=True)

    email = serializers.EmailField(read_only=True)

    picture = serializers.ImageField(read_only=True)


class BusinessCreateSerializer(serializers.Serializer):
    """Business create serializer."""

    name = serializers.CharField(max_length=200)

    description = serializers.CharField()

    city = serializers.CharField(max_length=200)

    sub_city = serializers.CharField(max_length=200)

    type = serializers.ChoiceField(choices=BusinessType.choices)

    owners = serializers.ListField(required=False)
