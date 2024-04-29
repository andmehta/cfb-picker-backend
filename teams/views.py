from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from rest_framework import viewsets, permissions

from teams.models import Team
from teams.serializers import TeamSerializer


class TeamsView(viewsets.ReadOnlyModelViewSet):
    """This is setup to run .as_view({"get": "list"}) so the HTTP method GET is already defined in DRF
    POST is defined as NOT ALLOWED since it's the ReadOnlyModelViewSet"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamsListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'teams_list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return super().get_queryset().prefetch_related("home_games", "away_games")

