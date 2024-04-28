from django.urls import path

from teams.views import TeamsView

urlpatterns = [
    path("", TeamsView.as_view({"get": "list"}), name="api_teams_list"),
    path("<int:pk>/", TeamsView.as_view({"get": "retrieve"}), name="api_teams_retrieve"),
]
