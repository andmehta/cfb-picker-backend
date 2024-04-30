from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import viewsets, permissions

from games.forms import PredictionForm
from games.models import Game, GamePrediction
from games.serializers import GameSerializer
from teams.models import Team


class GamesView(viewsets.ReadOnlyModelViewSet):
    """This is set up to run .as_view({"get": "list"}) or {"get": "retrieve"} so the HTTP method GET
    is already defined in DRF
    POST/PUT/DELETE is defined as NOT ALLOWED since it's the ReadOnlyModelViewSet"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required
def game_detail(request, pk=1):
    game = Game.objects.get(pk=pk)
    previous_form = None
    if request.method == 'POST':
        previous_form = PredictionForm(request.POST)
        if previous_form.is_valid():
            previous_form.instance.game_id = pk
            previous_form.instance.user_id = request.user.pk
            prediction = previous_form.save()
            messages.success(request, f"Successfully saved {prediction}")
            return redirect(reverse("teams_list"))
    try:
        game_prediction = GamePrediction.objects.get(game=game, user=request.user)
    except GamePrediction.DoesNotExist:
        game_prediction = None
    if game_prediction:
        # if this user has already predicted this game, show that
        initial_data = {
            "winner": game_prediction.winner,
            "loser": game_prediction.loser,
            "winning_score": game_prediction.winning_score,
            "losing_score": game_prediction.losing_score,
        }
        # weird case that a new prediction supersedes a recent failed form.
        # This will just render the disabled form, which I'd prefer
        form = PredictionForm(initial=initial_data)
        for field, value in form.fields.items():
            value.disabled = True
    else:
        form = previous_form or PredictionForm()
        filtered = Team.objects.filter(pk__in=(game.home_team.id, game.away_team.id))
        form.fields["winner"].queryset = filtered
        form.fields["loser"].queryset = filtered
    return render(request, "game_detail.html", context={"game": game, "form": form})
