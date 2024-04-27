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
        return f"{self.away_team} at {self.home_team}{f' at {self.kickoff}' if self.kickoff else ''}"
