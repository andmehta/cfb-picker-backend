"""
Top Level URLs for the cfbpicker project
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("teams/", include("teams.urls")),
]
