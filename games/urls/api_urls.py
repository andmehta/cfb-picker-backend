from django.urls import path

from games.views import GamesView

urlpatterns = [
    path("", GamesView.as_view({"get": "list"}), name="games_list"),
    path("<int:pk>/", GamesView.as_view({"get": "retrieve"}), name="games_get"),
]