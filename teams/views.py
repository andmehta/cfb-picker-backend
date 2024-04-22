from rest_framework import viewsets
from teams.models import Team
from teams.serializers import TeamSerializer


class TeamsView(viewsets.ReadOnlyModelViewSet):
    """This is setup to run .as_view({"get": "list"}) so the HTTP method GET is already defined in DRF
    POST is defined as NOT ALLOWED since it's the ReadOnlyModelViewSet"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
