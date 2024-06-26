from django.core.validators import RegexValidator
from django.db import models


class HexColorField(models.CharField):
    default_validators = [
        RegexValidator(
            regex='^#[a-fA-F0-9]{6}$',
            message='Enter a valid hex color (e.g. #RRGGBB)',
            code='invalid_color'
        )
    ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)


class Team(models.Model):
    """Database Table for Football teams.
    This is expected to get added with a Fixture, and not created/edited by Users"""

    name = models.CharField(null=False, max_length=40)  # University of Alabama
    nickname = models.CharField(max_length=30)  # Bama
    abbreviation = models.CharField(max_length=5)  # UA
    mascot = models.CharField(max_length=25)
    conference = models.CharField(max_length=12)
    primary_color = HexColorField()
    secondary_color = HexColorField()

    def __str__(self):
        return self.nickname

    @property
    def games(self):
        """Combine away and home games"""
        # local import to avoid circular dependencies
        from games.models import Game
        from django.db.models import Q
        return Game.objects.filter(Q(home_team=self) | Q(away_team=self)).all().order_by("kickoff")
