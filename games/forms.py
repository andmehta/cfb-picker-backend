from django.forms import ModelForm, HiddenInput, CharField, IntegerField
from games.models import GamePrediction


class PredictionForm(ModelForm):
    class Meta:
        model = GamePrediction
        fields = ["winner", "loser", "winning_score", "losing_score"]

    winning_score = IntegerField(max_value=99, min_value=0)
    losing_score = IntegerField(max_value=98, min_value=0)
