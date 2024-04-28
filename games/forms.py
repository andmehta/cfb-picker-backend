from django.forms import ModelForm, IntegerField, ValidationError
from games.models import GamePrediction


class PredictionForm(ModelForm):
    class Meta:
        model = GamePrediction
        fields = ["winner", "loser", "winning_score", "losing_score"]

    winning_score = IntegerField(max_value=99, min_value=0)
    losing_score = IntegerField(max_value=98, min_value=0)

    def clean(self):
        cleaned_data = super().clean()
        winner = cleaned_data.get('winner')
        loser = cleaned_data.get('loser')

        if winner == loser:
            raise ValidationError("Winner and loser must be different teams.")

        winning_score = cleaned_data.get("winning_score")
        losing_score = cleaned_data.get("losing_score")

        if winning_score <= losing_score:
            raise ValidationError("You cannot lose a game with a higher score than your opponent.")

        return cleaned_data
