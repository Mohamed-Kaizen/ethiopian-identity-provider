"""Django base settings for Ethiopian Identity Provider project."""
import pathlib
from datetime import datetime, timedelta
from typing import List

from decouple import Csv, config
from dj_database_url import parse as db_url
from django.utils.translation import gettext_lazy as _

# General
# ------------------------------------------------------------------------------
BASE_DIR = pathlib.Path().absolute()

TEMPLATES_DIR = [BASE_DIR.joinpath("templates")]

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = config("DEBUG", cast=bool)

ADMIN_URL = config("ADMIN_URL", cast=str, default="admin")

# using python-decouple to hide the SECRET_KEY
SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(str))

SITE_ID = 1

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "etp.urls"

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "etp.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "axes",
    "import_export",
    "corsheaders",
    "storages",
    "drf_yasg",
    "django_filters",
    "oauth2_provider",
    "reversion",
    "reversion_compare",
    "django_countries",
]

LOCAL_APPS = ["users.apps.UsersConfig"]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # django-cors-headers
    "whitenoise.middleware.WhiteNoiseMiddleware",  # whitenoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",  # django-axes
]

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = (
    "axes.backends.AxesBackend",
    "oauth2_provider.backends.OAuth2Backend",
    "django.contrib.auth.backends.ModelBackend",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.CustomUser"

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "home"

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "sign_in"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django  # noqa: B950
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa: B950
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    {
        "NAME": "pwned_passwords_django.validators.PwnedPasswordsValidator",
        "OPTIONS": {
            "error_message": "Oh no — pwned! This password has been seen "
            "%(amount)d times before",
            "help_message": "Your password can't be a commonly used password.",
        },
    },
]

# STATIC (CSS, JavaScript, Images)
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS  # noqa: B950
STATICFILES_DIRS = [BASE_DIR.joinpath("static")]

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = BASE_DIR.joinpath("static_root")

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = BASE_DIR.joinpath("media")

# ADMIN
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("Mohamed Nesredin", "m.n.kaizen@gmail.com")]

# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# Internationalization
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Africa/Addis_Ababa"

# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [BASE_DIR.joinpath("local")]

LANGUAGES = (("en", _("English")), ("ar", _("Arabic")), ("am", _("Amharic")))

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND  # noqa: B950
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": TEMPLATES_DIR,
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors  # noqa: B950
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "users.context_processors.from_settings",
            ],
        },
    }
]

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = not DEBUG

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = not DEBUG

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = not DEBUG


# Email
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = config("EMAIL_USER", cast=str)
    EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD", cast=str)

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {
    "default": config("DATABASE_URL", cast=db_url, default="sqlite:///db.sqlite3")
}

# LOGGER
# ------------------------------------------------------------------------------
LOG_DATE_FORMAT = datetime.now().strftime("%B %d, %Y")
CONSOLE_LOGGING_FILE = BASE_DIR.joinpath(f"logs/django_{LOG_DATE_FORMAT}.log")

LOGGING = {
    "version": 1,
    "loggers": {
        # root logger
        "": {"level": "INFO", "handlers": ["console", "mail_admins", "file"]},
        "django": {
            "handlers": ["console", "mail_admins", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "django.server": {"propagate": True},
    },
    "formatters": {
        "my_formatter": {
            "format": "{asctime} {levelname} {threadName} {name} {filename}"
            " {funcName} {module} {message}",
            "style": "{",
        },
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
        "console": {"class": "logging.StreamHandler", "formatter": "my_formatter"},
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": CONSOLE_LOGGING_FILE,
            "mode": "a",
            "encoding": "utf-8",
            "formatter": "my_formatter",
            "backupCount": 5,
            "maxBytes": 10485760,
        },
    },
}

# Third-Party Settings
# djangorestframework
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
}

# whitenoise
# ------------------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS.insert(0, "whitenoise.runserver_nostatic")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# django-extensions
# ------------------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS.append("django_extensions")


# django-debug-toolbar
# ------------------------------------------------------------------------------
if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config  # noqa: B950
    DEBUG_TOOLBAR_CONFIG = {"SHOW_TEMPLATE_CONTEXT": True}

    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips  # noqa: B950
    INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

    # displaying panels for django debug
    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ]

# django-axes
# ------------------------------------------------------------------------------
AXES_COOLOFF_TIME = timedelta(minutes=60) if not DEBUG else timedelta(minutes=5)
AXES_FAILURE_LIMIT = 5
AXES_USE_USER_AGENT = True

# django-cors-headers
# ------------------------------------------------------------------------------
# https://github.com/adamchainz/django-cors-headers#cors_origin_allow_all
# Todo: Change this in production
CORS_ORIGIN_ALLOW_ALL = True

# django-storages
# ------------------------------------------------------------------------------
if not DEBUG:
    DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"

    DROPBOX_OAUTH2_TOKEN = config("DROPBOX_OAUTH2_TOKEN", cast=str)

    DROPBOX_ROOT_PATH = "media"

# django-oauth-toolkit
# ------------------------------------------------------------------------------
OAUTH2_PROVIDER = {
    "OAUTH2_VALIDATOR_CLASS": "etp.validators.AxesOAuth2Validator",
    "SCOPES": {
        "user": "Read your user info like username, email, profile picture",
        "user:profile": "Read your personal info",
        "business:accepted": "Read all accepted business",
        "business:requested": "Read all requested business",
        "business:write": "Write new business request",
        "renew:write": "Write new renew request",
    },
    # "REQUEST_APPROVAL_PROMPT": "auto",  # to ask user for authorization only once
}

# django-reversion-compare
# ------------------------------------------------------------------------------
ADD_REVERSION_ADMIN = True
# optional settings:
REVERSION_COMPARE_FOREIGN_OBJECTS_AS_ID = False
REVERSION_COMPARE_IGNORE_NOT_REGISTERED = False

# Your settings...
# ------------------------------------------------------------------------------

if DEBUG:

    ENVIRONMENT_NAME = _("Dev")

    ENVIRONMENT_COLOR = "red"

else:

    ENVIRONMENT_NAME = _("Production")

    ENVIRONMENT_COLOR = "green"

CUSTOM_RESERVED_NAMES: List[str] = []

HOME_PAGE_URL = config("HOME_PAGE_URL", cast=str)
