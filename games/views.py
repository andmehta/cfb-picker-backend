from django.shortcuts import render
from rest_framework import viewsets
from games.models import Game
from games.serializers import GameSerializer


class GamesView(viewsets.ReadOnlyModelViewSet):
    """This is set up to run .as_view({"get": "list"}) or {"get": "retrieve"} so the HTTP method GET
    is already defined in DRF
    POST/PUT/DELETE is defined as NOT ALLOWED since it's the ReadOnlyModelViewSet"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, "game_detail.html", context={"game": game})