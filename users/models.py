"""Collection of model."""
import uuid
from typing import Any

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from .utils import unique_personal_identity_number


def user_upload_to(instance: "CustomUser", filename: str) -> str:
    """A help Function to change the image upload path.

    Args:
        instance: django model
        filename: the uploaded file name

    Returns:
        path in string format
    """
    return f"images/profile_pics/{instance.username}/{filename}"


def fingerprint_upload_to(instance: "Fingerprint", filename: str) -> str:
    """A help Function to change the image upload path.

    Args:
        instance: django model
        filename: the uploaded file name

    Returns:
        path in string format
    """
    return f"images/profile_pics/{instance.user.username}/fingerprint/{filename}"


class Status(models.TextChoices):
    """Enum class for Status."""

    Requested = ("Requested", _("Requested"))

    Accepted = ("Accepted", _("Accepted"))


class CustomUser(AbstractUser):
    """Reference user model."""

    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name=_("unique id")
    )

    pin = models.CharField(
        verbose_name=_("personal identity number"),
        max_length=25,
        unique=True,
        editable=False,
    )

    email = models.EmailField(verbose_name=_("email address"), unique=True)

    full_name = models.CharField(verbose_name=_("full name"), max_length=300)

    picture = models.ImageField(
        verbose_name=_("picture"),
        default="images/default/pic.png",
        upload_to=user_upload_to,
    )

    phone_number = models.CharField(verbose_name=_("phone number"), max_length=10)

    date_of_birth = models.DateTimeField(verbose_name=_("date of birth"), null=True)

    born = CountryField(verbose_name=_("born"))

    nationality = CountryField(verbose_name=_("nationality"))

    expired_at = models.DateTimeField(
        verbose_name=_("expired at"),
        default=timezone.now() + timezone.timedelta(days=365),
    )

    class Meta:
        """Meta data."""

        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self: "CustomUser") -> str:
        """It return readable name for the model."""
        return f"{self.username}"

    def age(self: "CustomUser") -> str:
        """A function that display age of user in django admin page."""
        try:
            return f"{timezone.now().year - self.date_of_birth.year}"

        except Exception as error:
            print(error)
            return ""


class Address(models.Model):
    """Reference address model."""

    user = models.ForeignKey(
        CustomUser,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="addresses",
        db_index=True,
    )

    country = CountryField(verbose_name=_("country"))

    city = models.CharField(verbose_name=_("city"), max_length=100)

    street = models.CharField(verbose_name=_("street"), max_length=100)

    house_number = models.CharField(verbose_name=_("house number"), max_length=100)

    class Meta:
        """Meta data."""

        verbose_name = _("address")
        verbose_name_plural = _("addresses")

    def __str__(self: "Address") -> str:
        """It return readable name for the model."""
        return f"{self.user} address"


class Fingerprint(models.Model):
    """Reference fingerprint model."""

    user = models.ForeignKey(
        CustomUser,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="fingerprints",
        db_index=True,
    )

    picture = models.ImageField(
        verbose_name=_("picture"), upload_to=fingerprint_upload_to
    )

    class Meta:
        """Meta data."""

        verbose_name = _("fingerprint")
        verbose_name_plural = _("fingerprints")

    def __str__(self: "Fingerprint") -> str:
        """It return readable name for the model."""
        return f"{self.user} fingerprint"


class Renew(models.Model):
    """Reference renew model."""

    user = models.ForeignKey(
        CustomUser,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="renews",
        db_index=True,
    )

    status = models.CharField(
        verbose_name=_("status"),
        choices=Status.choices,
        default=Status.Requested,
        max_length=20,
    )

    create_at = models.DateTimeField(verbose_name=_("created_at"), auto_now_add=True)

    class Meta:
        """Meta data."""

        verbose_name = _("renew")
        verbose_name_plural = _("renews")

    def __str__(self: "Renew") -> str:
        """It return readable name for the model."""
        return f"{self.user} ask for renew"


@receiver(pre_save, sender=CustomUser)
def event_pin(sender: CustomUser, instance: CustomUser, **kwargs: Any) -> None:
    """Signal for CustomUser."""
    if not instance.pin:
        instance.pin = unique_personal_identity_number()
