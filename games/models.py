from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from teams.models import Team


class Season(models.Model):
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.start.year} season"


class Game(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name="home_games")
    away_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name="away_games")
    location = models.CharField()  # stadium name
    kickoff = models.DateTimeField(null=True)  # split into date and time?

    def __str__(self):
        return f"{self.away_team} at {self.home_team}{f' on {self.kickoff_string}' if self.kickoff else ''}"

    @property
    def kickoff_string(self):
        """pre-formatted kickoff string for convenience"""
        return self.kickoff.strftime("%m-%d-%Y at %H:%M")

    def user_prediction(self, user: User, winner: Team, loser: Team, winning_score: int, losing_score: int):
        """Create a new prediction for this game, could raise a DB error if this prediction already exists"""
        # validate teams are part of this game
        if not winner == self.home_team or not winner == self.away_team:
            raise ValidationError("Winner must be one of the teams playing")
        if not loser == self.home_team or not loser == self.away_team:
            raise ValidationError("Loser must be one of the teams playing")
        # is it more efficient to let this fail, or to test if the object exists already?
        new_prediction = GamePrediction(user=user, game=self, winner=winner, loser=loser, winning_score=winning_score,
                                        losing_score=losing_score)
        new_prediction.save()


class GamePrediction(models.Model):
    """Users make predictions on games, this model saves that decision"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, related_name="predictions")
    winner = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="predicted_wins")
    loser = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="predicted_losses")
    winning_score = models.PositiveSmallIntegerField()
    losing_score = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("user", "game")
