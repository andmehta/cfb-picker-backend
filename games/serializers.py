from rest_framework.serializers import ModelSerializer
from games.models import Game


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
