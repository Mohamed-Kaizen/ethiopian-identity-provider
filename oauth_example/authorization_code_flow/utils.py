"""Collection of utils functions."""
import secrets
import string

chars_string = string.ascii_lowercase + string.digits + string.ascii_uppercase


def unique_state_code() -> str:
    """Create state code."""
    return "".join(secrets.choice(chars_string) for _ in range(7))
