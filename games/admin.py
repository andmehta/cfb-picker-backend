from django.contrib import admin
from games.models import Season, Game


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("start", "end")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("home_team", "away_team", "kickoff")
    list_filter = ("home_team__name", )
