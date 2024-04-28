"""
Top Level URLs for the cfbpicker project
"""

from django.contrib import admin
from django.urls import path, include

api_patterns = [
    path("teams/", include("teams.urls.api_urls")),
    path("games/", include("games.urls.api_urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("teams/", include("teams.urls.site_urls")),
    path("games/", include("games.urls.site_urls")),
    path("api/v1/", include(api_patterns))
]
