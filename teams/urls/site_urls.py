from django.urls import path
from teams.views import TeamsListView

urlpatterns = [
    path("", TeamsListView.as_view(), name='teams_list'),
]
