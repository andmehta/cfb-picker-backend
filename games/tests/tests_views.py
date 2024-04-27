from django.core.management import call_command
from django.test import TestCase


class TestGamesViewTestCase(TestCase):

    def setUp(self):
        """First set up Teams and Games data in the database with a fixture"""
        call_command("loaddata", "initial_teams_data")
        call_command("loaddata", "2024_season")
        self.expected_keys = (
            "id", "season", "home_team", "away_team", "home_team", "location", "kickoff")

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
