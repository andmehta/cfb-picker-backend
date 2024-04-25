from django.core.management import call_command
from django.test import TestCase


class TestTeamsViewTestCase(TestCase):

    def setUp(self):
        """First set up Teams data in the database with a fixture"""
        call_command("loaddata", "initial_teams_data")

    def test_view_with_objects__list_returned(self):
        """first add objects to the DB, then get the endpoint and see a list"""
        response = self.client.get("/teams/")
        if not response.status_code == 200:
            self.fail(f"status code did not equal 200 actual = {response.status_code}")
        first_obj = response.data[0]
        expected_keys = (
        "name", "nickname", "id", "abbreviation", "mascot", "conference", "primary_color", "secondary_color")
        for key in first_obj.keys():
            self.assertTrue(key in expected_keys)