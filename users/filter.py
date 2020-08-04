"""Collection of filters."""
from django_filters import rest_framework as filters

from .models import CustomUser


class UserFilter(filters.FilterSet):
    """Filter for user model."""

    class Meta:
        """Meta data."""

        model = CustomUser
        fields = ("nationality",)
