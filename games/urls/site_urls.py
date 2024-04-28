"""These views will render a template to choose a game and choose the winner and score"""
from django.urls import path
from games.views import game_detail

urlpatterns = [
    path("<int:pk>/", game_detail, name='game_detail'),
]
