"""Collection of utils functions."""
import secrets
import string


def unique_personal_identity_number() -> str:
    """Create unique personal identity number."""
    number = "".join(secrets.choice(string.digits) for _ in range(12))
    return f"{number[:3]}-{number[3:6]}-{number[6:9]}-{number[9:12]}"
