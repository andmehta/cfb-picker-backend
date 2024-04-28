from rest_framework import viewsets
from teams.models import Team
from games.models import Game
from teams.serializers import TeamSerializer
from django.shortcuts import render


class TeamsView(viewsets.ReadOnlyModelViewSet):
    """This is setup to run .as_view({"get": "list"}) so the HTTP method GET is already defined in DRF
    POST is defined as NOT ALLOWED since it's the ReadOnlyModelViewSet"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


def teams_list(request):
    teams = Team.objects.all().prefetch_related("home_games", "away_games")

    return render(request, 'teams_list.html', {'teams': teams})
