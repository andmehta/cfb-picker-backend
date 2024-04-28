from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase


class TestTeamsViewTestCase(TestCase):

    def setUp(self):
        """First set up Teams data in the database with a fixture"""
        call_command("loaddata", "initial_teams_data")
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.force_login(self.user)

    def test_list_view_with_objects__list_returned(self):
        """first add objects to the DB, then get the endpoint and see a list"""
        response = self.client.get("/api/v1/teams/")
        if not response.status_code == 200:
            self.fail(f"status code did not equal 200 actual = {response.status_code}")
        self.assertIsInstance(response.data, list)
        first_obj = response.data[0]
        self.assertIsInstance(first_obj, dict)
        expected_keys = (
            "name", "nickname", "id", "abbreviation", "mascot", "conference", "primary_color", "secondary_color")
        for key in first_obj.keys():
            self.assertTrue(key in expected_keys)

    def test_retrieve_view_with_objects__object_returned(self):
        """See we can get an individual team as well"""
        response = self.client.get("/api/v1/teams/4/")  # include a PK
        if not response.status_code == 200:
            self.fail(f"status code did not equal 200 actual = {response.status_code}")
        self.assertIsInstance(response.data, dict)
        expected_keys = (
            "name", "nickname", "id", "abbreviation", "mascot", "conference", "primary_color", "secondary_color")
        for key in response.data.keys():
            self.assertTrue(key in expected_keys)
