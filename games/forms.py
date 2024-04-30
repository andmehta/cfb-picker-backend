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
        winning_score = cleaned_data.get("winning_score")
        losing_score = cleaned_data.get("losing_score")
        errors = []

        if winner == loser:
            errors.append("Winner and loser must be different teams.")

        if winning_score <= losing_score:
            errors.append("Winning score must be higher than the losing score")

        if errors:
            raise ValidationError(errors)

        return cleaned_data
