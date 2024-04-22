from django.contrib import admin
from teams.models import Team


@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):
    model = Team
    list_display = ("name", "nickname", "mascot")
    search_fields = ("name",)
