"""Admin module for users app."""
from typing import Dict, Optional

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest
from django.forms.models import ModelFormMetaclass
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ExportActionModelAdmin
from oauth2_provider.models import AccessToken, Application, Grant, RefreshToken
from reversion_compare.admin import CompareVersionAdmin
from reversion_compare.helpers import patch_admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Address, CustomUser, Fingerprint


class UserResource(resources.ModelResource):
    """ModelResource is Resource subclass for handling Django models."""

    class Meta:
        """Meta data."""

        model = CustomUser
        fields = ("username", "email", "date_joined", "last_login")

        export_order = ("username", "email", "date_joined", "last_login")


class AddressInline(admin.StackedInline):
    """Inline for Address model."""

    model = Address
    extra = 0


class FingerprintInline(admin.TabularInline):
    """Inline for Fingerprint model."""

    model = Fingerprint
    extra = 0


@admin.register(CustomUser)
class CustomUserAdmin(ExportActionModelAdmin, CompareVersionAdmin, UserAdmin):
    """Configure the users app in admin page."""

    inlines = [AddressInline, FingerprintInline]

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    resource_class = UserResource
    model = CustomUser
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2",)},
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "full_name",
                    "email",
                    "date_of_birth",
                    "born",
                    "nationality",
                    "picture",
                )
            },
        ),
        (_("Permissions"), {"fields": ("is_superuser", "is_staff", "groups")}),
    )

    fieldsets = (
        (None, {"fields": ("username", "pin")}),
        (
            _("Personal info"),
            {
                "classes": ("collapse",),
                "fields": (
                    "full_name",
                    "email",
                    "date_of_birth",
                    "age",
                    "born",
                    "nationality",
                    "picture",
                    "rendered_picture",
                ),
            },
        ),
        (
            _("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "classes": ("collapse",),
                "fields": ("last_login", "date_joined", "expired_at"),
            },
        ),
    )

    list_display = (
        "username",
        "full_name",
        "nationality",
        "born",
        "expired_at",
    )

    ordering = (
        "username",
        "full_name",
        "nationality",
        "born",
        "expired_at",
    )

    list_filter = ("last_login", "expired_at", "nationality", "born")

    date_hierarchy = "date_joined"

    search_fields = ("username", "full_name")

    readonly_fields = (
        "rendered_picture",
        "last_login",
        "date_joined",
        "age",
        "expired_at",
        "pin",
    )

    def rendered_picture(self: "CustomUserAdmin", obj: "CustomUser") -> str:
        """A function that render the picture in django admin page."""
        return mark_safe(  # noqa S703
            f'<img src="{obj.picture.url}" width=40 height=40 style="border-radius: 9999px;"/>'  # noqa B950
        )

    def get_form(
        self: "CustomUserAdmin",
        request: WSGIRequest,
        obj: Optional[CustomUser] = None,
        **kwargs: Dict,
    ) -> ModelFormMetaclass:
        """Override the default form."""
        form = super().get_form(request, obj, **kwargs)

        is_superuser = request.user.is_superuser

        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                "is_superuser",
                "is_staff",
                "is_active",
                "groups",
                "user_permissions",
            }

        for field in disabled_fields:

            if field in form.base_fields:

                form.base_fields[field].disabled = True

        return form


patch_admin(Application)
patch_admin(Grant)
patch_admin(AccessToken)
patch_admin(RefreshToken)


admin.site.site_title = _("Ethiopian Identity Administrator site admin")
admin.site.site_header = _("Ethiopian Identity Administrator Dashboard")
admin.site.index_title = _("Welcome to Ethiopian Identity Administrator")
