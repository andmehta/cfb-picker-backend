"""These views will render a template to choose a game and choose the winner and score"""
from django.urls import path
from games.views import GameDetailView

urlpatterns = [
    path("<int:pk>/", GameDetailView.as_view(), name='game_detail'),
]
