import json
from django.core.serializers import serialize
from teams.models import Team

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a JSON file for the contents of the database in the Team table'

    def handle(self, *args, **options):
        # Query all objects from the database table
        self.stdout.write("Creating a fixture of the Teams table")
        queryset = Team.objects.all()

        # Serialize the queryset into JSON format
        serialized_data = serialize('json', queryset)

        # Convert the serialized data into Python objects
        data = json.loads(serialized_data)
        self.stdout.write("writing data to file")

        # Write the serialized data to a fixture file
        with open('./output/initial_teams_data.json', 'w') as f:
            json.dump(data, f, indent=2)
        self.stdout.write("Finished creating fixture")
