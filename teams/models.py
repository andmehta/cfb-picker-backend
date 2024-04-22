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

    name = models.CharField(null=False)  # University of Alabama
    nickname = models.CharField()  # Bama
    abbreviation = models.CharField()  # UA
    mascot = models.CharField()
    conference = models.CharField()
    primary_color = HexColorField()
    secondary_color = HexColorField()


