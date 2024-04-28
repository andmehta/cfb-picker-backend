from django.urls import path
from teams.views import teams_list

urlpatterns = [
    path("", teams_list, name='teams_list'),
]
