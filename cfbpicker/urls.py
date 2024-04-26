"""
Top Level URLs for the cfbpicker project
"""

from django.contrib import admin
from django.urls import path, include

api_patterns = [
    path("teams/", include("teams.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_patterns))
]
