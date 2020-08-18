"""Ethiopian Identity Provider URL Configuration."""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import home, sign_out

schema_view = get_schema_view(
    openapi.Info(
        title=_("Ethiopian Identity Provider API"),
        default_version=_("v1"),
        description=_("Ethiopian Identity Provider platform"),
        contact=openapi.Contact(email="m.n.kaizen@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = i18n_patterns(
    path(route="i18n/", view=include("django.conf.urls.i18n")),
    path("", home, name="home"),
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    path(
        ".well-known/security.txt",
        TemplateView.as_view(template_name="security.txt", content_type="text/plain",),
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain",),
    ),
    path("login/", LoginView.as_view(), name="sign_in"),
    path("accounts/logout/", sign_out, name="sign_out"),
    path("api/users/", include("users.urls")),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    re_path(
        r"^docs(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    prefix_default_language=False,
)

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
