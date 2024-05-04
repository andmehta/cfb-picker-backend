#!/bin/bash
echo "migrating database"
python manage.py migrate || exit 1

echo "trying to create the superuser"
# password comes from environment variable DJANGO_SUPERUSER_PASSWORD
# try to create the superuser, but if that fails, just move on
python manage.py createsuperuser --noinput --username admin1 --email admin@example.com || true

python manage.py loaddata initial_teams_data

python manage.py loaddata 2024_season

# TODO replace this with a real webserver eventually
python manage.py runserver 0.0.0.0:8000