# Generated by Django 5.0.4 on 2024-04-22 19:31

import teams.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField()),
                ("nickname", models.CharField()),
                ("abbreviation", models.CharField()),
                ("mascot", models.CharField()),
                ("conference", models.CharField()),
                ("primary_color", teams.models.HexColorField(max_length=7)),
                ("secondary_color", teams.models.HexColorField(max_length=7)),
            ],
        ),
    ]
