"""
Top Level URLs for the cfbpicker project
"""

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

api_patterns = [
    path("teams/", include("teams.urls.api_urls")),
    path("games/", include("games.urls.api_urls")),
]

urlpatterns = [
    # Landing page redirects to teams list for now
    path("", lambda request: redirect("teams_list")),
    path("admin/", admin.site.urls),
    path("teams/", include("teams.urls.site_urls")),
    path("games/", include("games.urls.site_urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/v1/", include(api_patterns)),
]
