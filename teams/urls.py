from django.urls import path

from teams.views import TeamsView

urlpatterns = [
    path("", TeamsView.as_view({"get": "list"}), name="index"),
]