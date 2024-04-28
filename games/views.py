from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, FormView
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


class GameDetailView(LoginRequiredMixin, DetailView, FormView):
    model = Game
    template_name = "game_detail.html"
    context_object_name = "game"
    # GameDetail, but Prediction Form
    form_class = PredictionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.object
        try:
            game_prediction = GamePrediction.objects.get(game=game, user=self.request.user)
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
            form = PredictionForm(initial=initial_data)
            for field, value in form.fields.items():
                value.disabled = True
        else:
            form = PredictionForm()
            filtered = Team.objects.filter(pk__in=(game.home_team.id, game.away_team.id))
            form.fields["winner"].queryset = filtered
            form.fields["loser"].queryset = filtered
        context["form"] = form
        return context

    def form_valid(self, form):
        game_id = self.kwargs["pk"]
        form.instance.game_id = game_id
        form.instance.user_id = self.request.user.pk
        form.save()
        return redirect(reverse("teams_list"))

