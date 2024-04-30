from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from games.models import GamePrediction, Game


class TestGamesViewTestCase(TestCase):

    def setUp(self):
        """First set up Teams and Games data in the database with a fixture"""
        call_command("loaddata", "initial_teams_data")
        call_command("loaddata", "2024_season")
        self.expected_keys = (
            "id", "season", "home_team", "away_team", "home_team", "location", "kickoff")
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.force_login(self.user)

    def test_list_view_with_objects__list_returned(self):
        """first add objects to the DB, then get the endpoint and see a list"""
        response = self.client.get("/api/v1/games/")
        if not response.status_code == 200:
            self.fail(f"status code did not equal 200 actual = {response.status_code}")
        self.assertIsInstance(response.data, list)
        first_obj = response.data[0]
        self.assertIsInstance(first_obj, dict)
        for key in first_obj.keys():
            self.assertTrue(key in self.expected_keys, f"key {key} not in expected keys")

    def test_retrieve_view_with_objects__object_returned(self):
        """See we can get an individual game as well"""
        response = self.client.get("/api/v1/games/4/")  # include a PK
        if not response.status_code == 200:
            self.fail(f"status code did not equal 200 actual = {response.status_code}")
        self.assertIsInstance(response.data, dict)
        for key in response.data.keys():
            self.assertTrue(key in self.expected_keys, f"key {key} not in expected keys")


class GameDetailViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_login(self.user)
        call_command("loaddata", "initial_teams_data")
        call_command("loaddata", "2024_season")
        self.game = Game.objects.first()

    def test_game_detail_get_existing_prediction(self):
        GamePrediction.objects.create(game=self.game, user=self.user, winner=self.game.home_team,
                                      loser=self.game.away_team, winning_score=1, losing_score=0)
        response = self.client.get(reverse("game_detail", kwargs={"pk": self.game.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "prediction_disabled.html")

    def test_game_detail_get_no_prediction(self):
        response = self.client.get(reverse("game_detail", kwargs={"pk": self.game.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "prediction_form.html")

    def test_game_detail_post_valid_form(self):
        data = {
            "winner": self.game.home_team.pk,
            "loser": self.game.away_team.pk,
            "winning_score": 2,
            "losing_score": 1,
        }
        response = self.client.post(reverse("game_detail", kwargs={"pk": self.game.pk}), data)
        self.assertRedirects(response, reverse("teams_list"))
        self.assertTrue(GamePrediction.objects.filter(game=self.game, user=self.user).exists())
